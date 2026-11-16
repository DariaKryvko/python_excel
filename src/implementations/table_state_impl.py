from collections import deque
from typing import override

from interfaces import Evaluator, TableState
from models import Cell, CellNode
from .evaluator_visitor_adapter import EvaluatorVisitorAdapter

class TableStateImpl(TableState):
    def __init__(self, evaluator: Evaluator | None = None):
        self.cells_map: dict[str, Cell] = {}
        self.dependency_graph_map: dict[str, CellNode] = {}
        self.evaluator: Evaluator = evaluator if evaluator is not None else EvaluatorVisitorAdapter()

    @override
    def get_cell(self, cell_id: str) -> Cell:
        norm_id = cell_id.strip().upper()
        if norm_id not in self.cells_map:
            return Cell(expression="", value=0, id=norm_id)
        return self.cells_map[norm_id]

    @override
    def get_non_empty_cells(self) -> dict[str, Cell]:
        return {
            cid: cell for cid, cell in self.cells_map.items()
            if cell.expression != ""
        }

    def _get_cell_values_dict(self) -> dict[str, int]:
        return {cid: cell.value for cid, cell in self.cells_map.items()}

    @override
    def update_cell(self, cell_id: str, new_expression: str) -> list[str]:
        norm_id = cell_id.strip().upper()
        clean_expr = new_expression.strip()

        # Transaction snapshot
        backup_cells = {
            cid: Cell(expression=c.expression, value=c.value, id=c.id)
            for cid, c in self.cells_map.items()
        }
        backup_graph = {
            cid: CellNode(
                dependencies_ids=list(node.dependencies_ids),
                dependants_ids=list(node.dependants_ids),
            )
            for cid, node in self.dependency_graph_map.items()
        }

        try:
            # 1. Evaluate new expression using current cell values
            cell_values = self._get_cell_values_dict()
            eval_result = self.evaluator.evaluate(clean_expr, cell_values)
            new_value = eval_result.new_value
            new_deps = [d.upper() for d in eval_result.new_dependencies]

            # 2. Check for direct self-reference
            if norm_id in new_deps:
                raise ValueError(f"Circular dependency detected: {norm_id} references itself")

            # 3. Tentatively update dependency graph
            if norm_id not in self.dependency_graph_map:
                self.dependency_graph_map[norm_id] = CellNode(dependencies_ids=[], dependants_ids=[])

            old_deps = list(self.dependency_graph_map[norm_id].dependencies_ids)
            for old_dep in old_deps:
                if old_dep in self.dependency_graph_map:
                    if norm_id in self.dependency_graph_map[old_dep].dependants_ids:
                        self.dependency_graph_map[old_dep].dependants_ids.remove(norm_id)

            self.dependency_graph_map[norm_id].dependencies_ids = new_deps
            for dep in new_deps:
                if dep not in self.dependency_graph_map:
                    self.dependency_graph_map[dep] = CellNode(dependencies_ids=[], dependants_ids=[])
                if norm_id not in self.dependency_graph_map[dep].dependants_ids:
                    self.dependency_graph_map[dep].dependants_ids.append(norm_id)

            # 4. Cycle detection in DAG (3-color DFS)
            color: dict[str, int] = {}

            def dfs_has_cycle(node: str) -> bool:
                color[node] = 1
                curr_node = self.dependency_graph_map.get(node)
                if curr_node:
                    for dependant in curr_node.dependants_ids:
                        if color.get(dependant, 0) == 1:
                            return True
                        if color.get(dependant, 0) == 0:
                            if dfs_has_cycle(dependant):
                                return True
                color[node] = 2
                return False

            for node in self.dependency_graph_map:
                if color.get(node, 0) == 0:
                    if dfs_has_cycle(node):
                        raise ValueError(f"Circular dependency detected involving {norm_id}")

            # 5. Update cell in cells_map
            self.cells_map[norm_id] = Cell(expression=clean_expr, value=new_value, id=norm_id)

            # 6. Find all transitive dependants of norm_id
            affected_nodes: set[str] = set()
            queue = deque([norm_id])
            while queue:
                curr = queue.popleft()
                node_obj = self.dependency_graph_map.get(curr)
                if node_obj:
                    for dep_id in node_obj.dependants_ids:
                        if dep_id not in affected_nodes:
                            affected_nodes.add(dep_id)
                            queue.append(dep_id)

            # 7. Topological sort on affected_nodes
            in_degree = {
                n: sum(1 for d in self.dependency_graph_map[n].dependencies_ids if d in affected_nodes)
                for n in affected_nodes
            }
            ready = deque([n for n in affected_nodes if in_degree[n] == 0])
            topo_order: list[str] = []

            while ready:
                u = ready.popleft()
                topo_order.append(u)
                node_obj = self.dependency_graph_map.get(u)
                if node_obj:
                    for v in node_obj.dependants_ids:
                        if v in affected_nodes:
                            in_degree[v] -= 1
                            if in_degree[v] == 0:
                                ready.append(v)

            # 8. Re-evaluate affected dependants in topological order
            for aff_id in topo_order:
                aff_cell = self.cells_map.get(aff_id)
                if aff_cell and aff_cell.expression != "":
                    res = self.evaluator.evaluate(aff_cell.expression, self._get_cell_values_dict())
                    aff_cell.value = res.new_value

            # All succeeded: commit and return updated cell IDs
            return [norm_id] + topo_order

        except Exception:
            # Transaction rollback on any error
            self.cells_map = backup_cells
            self.dependency_graph_map = backup_graph
            raise

    @override
    def load(self, cells: dict[str, Cell] | list[Cell]) -> None:
        self.cells_map.clear()
        self.dependency_graph_map.clear()
        if isinstance(cells, dict):
            for cell_id, cell in cells.items():
                expr = cell.expression if isinstance(cell, Cell) else str(cell)
                self.update_cell(cell_id, expr)
        elif isinstance(cells, list):
            for cell in cells:
                if hasattr(cell, "id") and cell.id:
                    self.update_cell(cell.id, cell.expression)

