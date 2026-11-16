from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from interfaces import Evaluator
from generated.GrammarLexer import GrammarLexer
from generated.GrammarParser import GrammarParser
from models import EvaluationResult

from .grammar_visitor import GrammarVisitor

class EvaluatorErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ValueError(f"Syntax error at {line}:{column}: {msg}")

class EvaluatorVisitorAdapter(Evaluator):
    def evaluate(self, expression: str, cell_values: dict[str, int]) -> EvaluationResult:
        if not expression or not expression.strip():
            return EvaluationResult(0, [])

        expr = expression.strip()
        if expr.startswith("="):
            expr = expr[1:].strip()
            if not expr:
                return EvaluationResult(0, [])

        input_stream = InputStream(expr)
        
        lexer = GrammarLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(EvaluatorErrorListener())

        token_stream = CommonTokenStream(lexer)

        parser = GrammarParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(EvaluatorErrorListener())

        tree = parser.expressionRoot()

        visitor = GrammarVisitor(cell_values)
        result, dependencies = visitor.visit(tree)
        
        normalized_deps = list(dict.fromkeys(d.upper() for d in dependencies))
        return EvaluationResult(result, normalized_deps)

