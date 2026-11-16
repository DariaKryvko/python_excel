from abc import ABC, abstractmethod

class SaveReaction(ABC):
    @abstractmethod
    def execute(self, filename: str) -> None:
        pass