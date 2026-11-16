from abc import ABC, abstractmethod

class CellUpdateReaction(ABC):
    @abstractmethod
    def execute(self, cell_id: str, new_text: str) -> None:
        pass