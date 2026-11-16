import sys
from typing import override
from PyQt6.QtWidgets import QApplication

from interfaces import ApplicationGUI, CellUpdateReaction, LoadReaction, SaveReaction
from .window import Window

class Qt6ApplicationGUI(ApplicationGUI):
    window: Window | None = None

    cell_update_reaction: CellUpdateReaction | None = None
    load_reaction: LoadReaction | None = None
    save_reaction: SaveReaction | None = None

    @override
    def register_cell_update_reaction(self, reaction: CellUpdateReaction):
        self.cell_update_reaction = reaction
        if self.window:
            self.window.cell_update_reaction = reaction

    @override
    def register_save_reaction(self, reaction: SaveReaction):
        self.save_reaction = reaction
        if self.window:
            self.window.save_reaction = reaction

    @override
    def register_load_reaction(self, reaction: LoadReaction):
        self.load_reaction = reaction
        if self.window:
            self.window.load_reaction = reaction

    @override
    def update_cell_text(self, cell_id: str, new_text: str):
        if self.window:
            self.window.update_cell_text(cell_id, new_text)

    def update_cell_display(self, cell_id: str, expression: str, value: int):
        if self.window:
            self.window.update_cell_display(cell_id, expression, value)

    def show_error(self, message: str):
        if self.window:
            self.window.show_error(message)

    def clear_table(self):
        if self.window:
            self.window.clear_table()

    @override
    def run(self):
        app = QApplication.instance() or QApplication(sys.argv)
        self.window = Window(self.cell_update_reaction, self.save_reaction, self.load_reaction)
        self.window.show()
        app.exec()
