from dataclasses import dataclass

@dataclass
class EvaluationResult:
    new_value: int
    new_dependencies: list[str]