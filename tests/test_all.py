import os
import tempfile
import unittest

from implementations import (
    Application,
    EvaluationCore,
    EvaluatorVisitorAdapter,
    TableStateImpl,
)
from implementations.coordinates import cell_id_to_coords, coords_to_cell_id
from interfaces import ApplicationGUI, CellUpdateReaction, LoadReaction, SaveReaction
from models import Cell

class DummyGUI(ApplicationGUI):
    def __init__(self):
        self.cells_display: dict[str, tuple[str, int]] = {}
        self.cells_text: dict[str, str] = {}
        self.errors: list[str] = []
        self.cleared = False
        self.cell_update_reaction: CellUpdateReaction | None = None
        self.save_reaction: SaveReaction | None = None
        self.load_reaction: LoadReaction | None = None

    def update_cell_text(self, cell_id: str, new_text: str) -> None:
        self.cells_text[cell_id] = new_text

    def update_cell_display(self, cell_id: str, expression: str, value: int) -> None:
        self.cells_display[cell_id] = (expression, value)
        self.cells_text[cell_id] = str(value) if expression != "" else ""

    def show_error(self, message: str) -> None:
        self.errors.append(message)

    def clear_table(self) -> None:
        self.cleared = True
        self.cells_display.clear()
        self.cells_text.clear()

    def register_cell_update_reaction(self, reaction: CellUpdateReaction) -> None:
        self.cell_update_reaction = reaction

    def register_save_reaction(self, reaction: SaveReaction) -> None:
        self.save_reaction = reaction

    def register_load_reaction(self, reaction: LoadReaction) -> None:
        self.load_reaction = reaction

    def run(self) -> None:
        pass


class TestCoordinates(unittest.TestCase):
    def test_roundtrip(self):
        cases = [(0, 0, "A1"), (0, 25, "Z1"), (0, 26, "AA1"), (9, 27, "AB10"), (99, 0, "A100")]
        for r, c, name in cases:
            self.assertEqual(coords_to_cell_id(r, c), name)
            self.assertEqual(cell_id_to_coords(name), (r, c))

    def test_case_insensitivity(self):
        self.assertEqual(cell_id_to_coords("a1"), (0, 0))
        self.assertEqual(cell_id_to_coords("ab10"), (9, 27))


class TestEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = EvaluatorVisitorAdapter()

    def test_arithmetic(self):
        res = self.evaluator.evaluate("3 + 4 * 2", {})
        self.assertEqual(res.new_value, 11)
        self.assertEqual(res.new_dependencies, [])

    def test_div_and_mod(self):
        res = self.evaluator.evaluate("17 div 5 + 17 mod 5", {})
        self.assertEqual(res.new_value, 3 + 2)

    def test_mmax_mmin(self):
        res = self.evaluator.evaluate("mmax(10, 5, 25, 3) - mmin(10, 5, 25, 3)", {})
        self.assertEqual(res.new_value, 25 - 3)

    def test_unary_operators(self):
        res = self.evaluator.evaluate("-5 + +10", {})
        self.assertEqual(res.new_value, 5)

    def test_cell_references_normalized(self):
        res = self.evaluator.evaluate("a1 + B2", {"A1": 10, "B2": 20})
        self.assertEqual(res.new_value, 30)
        self.assertEqual(sorted(res.new_dependencies), ["A1", "B2"])

    def test_empty_reference_defaults_to_zero(self):
        res = self.evaluator.evaluate("A1 + 5", {})
        self.assertEqual(res.new_value, 5)

    def test_empty_expression(self):
        res = self.evaluator.evaluate("", {})
        self.assertEqual(res.new_value, 0)
        self.assertEqual(res.new_dependencies, [])

    def test_syntax_error(self):
        with self.assertRaises(ValueError):
            self.evaluator.evaluate("3 + * 5", {})


class TestTableStateDAG(unittest.TestCase):
    def setUp(self):
        self.state = TableStateImpl()

    def test_basic_update_and_get(self):
        affected = self.state.update_cell("A1", "10")
        self.assertEqual(affected, ["A1"])
        cell = self.state.get_cell("A1")
        self.assertEqual(cell.value, 10)
        self.assertEqual(cell.expression, "10")

    def test_topological_sort_cascading(self):
        self.state.update_cell("A1", "5")
        self.state.update_cell("B1", "A1 * 2")  # 10
        self.state.update_cell("C1", "B1 + 3")   # 13
        self.state.update_cell("D1", "mmax(A1, B1, C1)")  # 13

        affected = self.state.update_cell("A1", "10")
        self.assertEqual(affected, ["A1", "B1", "C1", "D1"])
        self.assertEqual(self.state.get_cell("A1").value, 10)
        self.assertEqual(self.state.get_cell("B1").value, 20)
        self.assertEqual(self.state.get_cell("C1").value, 23)
        self.assertEqual(self.state.get_cell("D1").value, 23)

    def test_circular_dependency_self_reference(self):
        self.state.update_cell("A1", "5")
        with self.assertRaises(ValueError):
            self.state.update_cell("A1", "A1 + 1")
        # Transaction rolled back
        self.assertEqual(self.state.get_cell("A1").value, 5)

    def test_circular_dependency_indirect(self):
        self.state.update_cell("A1", "5")
        self.state.update_cell("B1", "A1 + 2")
        self.state.update_cell("C1", "B1 * 3")

        with self.assertRaises(ValueError):
            self.state.update_cell("A1", "C1 - 1")

        # Rollback check
        self.assertEqual(self.state.get_cell("A1").value, 5)
        self.assertEqual(self.state.get_cell("B1").value, 7)
        self.assertEqual(self.state.get_cell("C1").value, 21)

    def test_division_by_zero_rollback(self):
        self.state.update_cell("A1", "10")
        with self.assertRaises(ZeroDivisionError):
            self.state.update_cell("A1", "10 / 0")
        self.assertEqual(self.state.get_cell("A1").value, 10)

        # Division by zero in dependant during cascading update
        self.state.update_cell("B1", "20 / A1")  # 20 / 10 = 2
        with self.assertRaises(ZeroDivisionError):
            self.state.update_cell("A1", "0")  # causes B1 to divide by zero!
        # Both must be rolled back
        self.assertEqual(self.state.get_cell("A1").value, 10)
        self.assertEqual(self.state.get_cell("B1").value, 2)

    def test_clearing_cell(self):
        self.state.update_cell("A1", "10")
        self.state.update_cell("B1", "A1 + 5")
        self.assertEqual(self.state.get_cell("B1").value, 15)

        self.state.update_cell("A1", "")
        self.assertEqual(self.state.get_cell("A1").value, 0)
        self.assertEqual(self.state.get_cell("B1").value, 5)  # A1 is now 0


class TestApplicationAndReactions(unittest.TestCase):
    def setUp(self):
        self.state = TableStateImpl()
        self.gui = DummyGUI()
        self.app = Application(self.state, self.gui)
        self.app.run()

    def test_cell_update_reaction(self):
        assert self.gui.cell_update_reaction is not None
        self.gui.cell_update_reaction.execute("A1", "15")
        self.assertEqual(self.gui.cells_display["A1"], ("15", 15))
        self.assertEqual(self.gui.cells_text["A1"], "15")

        self.gui.cell_update_reaction.execute("B1", "A1 * 3")
        self.assertEqual(self.gui.cells_display["B1"], ("A1 * 3", 45))

    def test_error_handling_and_revert(self):
        assert self.gui.cell_update_reaction is not None
        self.gui.cell_update_reaction.execute("A1", "10")
        self.gui.cell_update_reaction.execute("B1", "A1")

        # Create cycle
        self.gui.cell_update_reaction.execute("A1", "B1")
        self.assertTrue(len(self.gui.errors) > 0)
        # Check that A1 was reverted in GUI display
        self.assertEqual(self.gui.cells_display["A1"], ("10", 10))

    def test_save_and_load_reaction(self):
        assert self.gui.cell_update_reaction is not None
        assert self.gui.save_reaction is not None
        self.gui.cell_update_reaction.execute("A1", "10")
        self.gui.cell_update_reaction.execute("B1", "A1 * 4")

        with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as f:
            temp_path = f.name

        try:
            self.gui.save_reaction.execute(temp_path)

            # Create fresh app
            new_state = TableStateImpl()
            new_gui = DummyGUI()
            new_app = Application(new_state, new_gui)
            new_app.run()

            assert new_gui.load_reaction is not None
            new_gui.load_reaction.execute(temp_path)

            self.assertEqual(new_state.get_cell("A1").value, 10)
            self.assertEqual(new_state.get_cell("B1").value, 40)
            self.assertEqual(new_gui.cells_display["A1"], ("10", 10))
            self.assertEqual(new_gui.cells_display["B1"], ("A1 * 4", 40))
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)


class TestQt6GUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import sys
        from PyQt6.QtWidgets import QApplication
        os.environ["QT_QPA_PLATFORM"] = "offscreen"
        cls.qapp = QApplication.instance() or QApplication(sys.argv)

    def test_window_view_switch_and_formula_bar(self):
        from implementations import Qt6ApplicationGUI
        from implementations.window import Window

        state = TableStateImpl()
        gui = Qt6ApplicationGUI()
        app = Application(state, gui)

        w = Window(
            Application.CellUpdateReactionImpl(state, app),
            Application.SaveReactionImpl(state, app),
            Application.LoadReactionImpl(state, app),
        )
        gui.window = w

        # Update cell display
        w.update_cell_display("A1", "10", 10)
        item_0_0 = w.table.item(0, 0)
        assert item_0_0 is not None
        self.assertEqual(item_0_0.text(), "10")

        # Switch to expressions view
        w.view_switcher.setCurrentIndex(1)
        item_0_0 = w.table.item(0, 0)
        assert item_0_0 is not None
        self.assertEqual(item_0_0.text(), "10")

        # Add formula in cell B1
        w.update_cell_display("B1", "A1 * 2", 20)
        # In expressions view, B1 displays the formula
        item_0_1 = w.table.item(0, 1)
        assert item_0_1 is not None
        self.assertEqual(item_0_1.text(), "A1 * 2")

        # Switch back to values view
        w.view_switcher.setCurrentIndex(0)
        item_0_1 = w.table.item(0, 1)
        assert item_0_1 is not None
        self.assertEqual(item_0_1.text(), "20")

        # Select cell B1, formula input should show expression
        w.table.setCurrentCell(0, 1)
        self.assertEqual(w.formula_input.text(), "A1 * 2")


if __name__ == "__main__":
    unittest.main()
