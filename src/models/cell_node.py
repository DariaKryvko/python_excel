from dataclasses import dataclass, field

@dataclass
class CellNode:
    dependencies_ids: list[str] = field(default_factory=list)
    dependants_ids: list[str] = field(default_factory=list)
