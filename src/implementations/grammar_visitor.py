# pyright: reportIncompatibleMethodOverride=false
from typing import Any

from generated.GrammarVisitor import GrammarVisitor as GrammarVisitorBase
from .evaluation_core import EvaluationCore

class GrammarVisitor(GrammarVisitorBase):
    def __init__(self, cells: dict[str, int]):
        super().__init__()
        self.cells = cells
        self.dependencies: set[str] = set()

    def visit(self, tree: Any) -> Any:
        return super().visit(tree)

    def prepare_binary_expr(self, ctx: Any) -> tuple[int, int]:
        left = int(self.visit(ctx.children[0]))
        right = int(self.visit(ctx.children[2]))
        return (left, right)

    def prepare_unary_expr(self, ctx: Any) -> int:
        return int(self.visit(ctx.children[1]))

    def prepare_function_expr(self, ctx: Any) -> list[int]:
        expressions = [ctx.children[i] for i in range(2, len(ctx.children), 2)]
        arguments = [int(self.visit(expr)) for expr in expressions]
        return arguments

    def visitExpressionRoot(self, ctx: Any) -> tuple[int, list[str]]:
        result = int(self.visit(ctx.expression()))
        return (result, list(self.dependencies))

    def visitNumberExpr(self, ctx: Any) -> int:
        return EvaluationCore.value(ctx.getText())

    def visitAddExpr(self, ctx: Any) -> int:
        left, right = self.prepare_binary_expr(ctx)
        return EvaluationCore.add(left, right)

    def visitSubExpr(self, ctx: Any) -> int:
        left, right = self.prepare_binary_expr(ctx)
        return EvaluationCore.subtract(left, right)

    def visitParenExpr(self, ctx: Any) -> int:
        return int(self.visit(ctx.expression()))

    def visitMultExpr(self, ctx: Any) -> int:
        left, right = self.prepare_binary_expr(ctx)
        return EvaluationCore.multiply(left, right)

    def visitDivExpr(self, ctx: Any) -> int:
        left, right = self.prepare_binary_expr(ctx)
        return EvaluationCore.divide(left, right)

    def visitDivFuncExpr(self, ctx: Any) -> int:
        left, right = self.prepare_binary_expr(ctx)
        return EvaluationCore.divide_func(left, right)

    def visitModExpr(self, ctx: Any) -> int:
        left, right = self.prepare_binary_expr(ctx)
        return EvaluationCore.modulo(left, right)

    def visitPlusExpr(self, ctx: Any) -> int:
        operand = self.prepare_unary_expr(ctx)
        return EvaluationCore.unary_plus(operand)

    def visitMinusExpr(self, ctx: Any) -> int:
        operand = self.prepare_unary_expr(ctx)
        return EvaluationCore.unary_minus(operand)

    def visitMminExpr(self, ctx: Any) -> int:
        operands = self.prepare_function_expr(ctx)
        return EvaluationCore.mmin(operands)

    def visitMmaxExpr(self, ctx: Any) -> int:
        operands = self.prepare_function_expr(ctx)
        return EvaluationCore.mmax(operands)

    def visitCellRefExpr(self, ctx: Any) -> int:
        cell_name = ctx.getText().upper()
        self.dependencies.add(cell_name)
        return EvaluationCore.cell_reference(cell_name, self.cells)
