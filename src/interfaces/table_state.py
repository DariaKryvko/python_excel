from abc import ABC, abstractmethod

from models import Cell

class TableState(ABC):
    @abstractmethod
    def get_cell(self, cell_id: str) -> Cell:
        pass
    
    @abstractmethod
    def update_cell(self, cell_id: str, new_expression: str) -> list[str]:
        pass
    
    @abstractmethod
    def load(self, cells: dict[str, Cell]) -> None:
        pass
    
    @abstractmethod
    def get_non_empty_cells(self) -> dict[str, Cell]:
        pass
