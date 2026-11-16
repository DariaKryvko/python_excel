from dataclasses import dataclass

@dataclass
class Cell:
    expression: str
    value: int
    id: str = ""

