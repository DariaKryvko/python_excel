from abc import ABC, abstractmethod

from .cell_update_reaction import CellUpdateReaction
from .save_reaction import SaveReaction
from .load_reaction import LoadReaction

class ApplicationGUI(ABC):
    @abstractmethod
    def update_cell_text(self, cell_id: str, new_text: str) -> None:
        pass
    
    @abstractmethod
    def register_cell_update_reaction(self, reaction: CellUpdateReaction) -> None:
        pass
    
    @abstractmethod
    def register_save_reaction(self, reaction: SaveReaction) -> None:
        pass
    
    @abstractmethod
    def register_load_reaction(self, reaction: LoadReaction) -> None:
        pass

    @abstractmethod
    def run(self) -> None:
        pass

    def update_cell_display(self, cell_id: str, expression: str, value: int) -> None:
        self.update_cell_text(cell_id, str(value))

    def show_error(self, message: str) -> None:
        pass

    def clear_table(self) -> None:
        pass
