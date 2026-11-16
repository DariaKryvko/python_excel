import csv
from typing import override

from interfaces import ApplicationGUI, CellUpdateReaction, LoadReaction, SaveReaction, TableState
from models import Cell

class CellUpdateReactionImpl(CellUpdateReaction):
    def __init__(self, table_state: TableState, app: "Application"):
        self.table_state: TableState = table_state
        self.app: "Application" = app

    @override
    def execute(self, cell_id: str, new_text: str) -> None:
        self.app.on_cell_update(cell_id, new_text)

class SaveReactionImpl(SaveReaction):
    def __init__(self, table_state: TableState, app: "Application"):
        self.table_state: TableState = table_state
        self.app: "Application" = app

    @override
    def execute(self, filename: str) -> None:
        self.app.on_save(filename)

class LoadReactionImpl(LoadReaction):
    def __init__(self, table_state: TableState, app: "Application"):
        self.table_state: TableState = table_state
        self.app: "Application" = app

    @override
    def execute(self, filename: str) -> None:
        self.app.on_load(filename)

class Application:
    CellUpdateReactionImpl = CellUpdateReactionImpl
    SaveReactionImpl = SaveReactionImpl
    LoadReactionImpl = LoadReactionImpl

    def __init__(self, table_state: TableState, gui: ApplicationGUI):
        self.table_state: TableState = table_state
        self.gui: ApplicationGUI = gui

    def on_cell_update(self, cell_id: str, new_text: str) -> None:
        prev_cell = self.table_state.get_cell(cell_id)
        prev_expr = prev_cell.expression
        prev_val = prev_cell.value

        try:
            affected_ids = self.table_state.update_cell(cell_id, new_text)
            for cid in affected_ids:
                cell = self.table_state.get_cell(cid)
                if hasattr(self.gui, "update_cell_display"):
                    self.gui.update_cell_display(cid, cell.expression, cell.value)
                else:
                    self.gui.update_cell_text(cid, str(cell.value))
        except Exception as e:
            if hasattr(self.gui, "show_error"):
                self.gui.show_error(f"Помилка в клітинці {cell_id}: {e}")
            if hasattr(self.gui, "update_cell_display"):
                self.gui.update_cell_display(cell_id, prev_expr, prev_val)
            else:
                self.gui.update_cell_text(cell_id, prev_expr)

    def on_save(self, filename: str) -> None:
        non_empty = self.table_state.get_non_empty_cells()
        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "expression"])
            for cid, cell in sorted(non_empty.items()):
                writer.writerow([cid, cell.expression])

    def on_load(self, filename: str) -> None:
        cells_to_load: list[tuple[str, str]] = []
        with open(filename, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            if header:
                if (
                    len(header) >= 2
                    and header[0].strip().lower() == "id"
                    and header[1].strip().lower() == "expression"
                ):
                    pass
                elif len(header) >= 2:
                    cells_to_load.append((header[0].strip(), header[1].strip()))
            for row in reader:
                if len(row) >= 2:
                    cells_to_load.append((row[0].strip(), row[1].strip()))

        cells_dict = {cid: Cell(expression=expr, value=0, id=cid) for cid, expr in cells_to_load}
        self.table_state.load(cells_dict)

        if hasattr(self.gui, "clear_table"):
            self.gui.clear_table()

        non_empty = self.table_state.get_non_empty_cells()
        for cid, cell in non_empty.items():
            if hasattr(self.gui, "update_cell_display"):
                self.gui.update_cell_display(cid, cell.expression, cell.value)
            else:
                self.gui.update_cell_text(cid, str(cell.value))

    def run(self) -> None:
        self.gui.register_cell_update_reaction(self.CellUpdateReactionImpl(self.table_state, self))
        self.gui.register_save_reaction(self.SaveReactionImpl(self.table_state, self))
        self.gui.register_load_reaction(self.LoadReactionImpl(self.table_state, self))
        self.gui.run()
