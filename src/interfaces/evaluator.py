from abc import ABC, abstractmethod

from models import EvaluationResult

class Evaluator(ABC):
    @abstractmethod
    def evaluate(self, expression: str, cell_values: dict[str, int]) -> EvaluationResult:
        pass