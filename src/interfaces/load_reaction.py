from abc import ABC, abstractmethod

class LoadReaction(ABC):
    @abstractmethod
    def execute(self, filename: str) -> None:
        pass