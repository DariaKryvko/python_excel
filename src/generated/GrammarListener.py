# Generated from Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#expressionRoot.
    def enterExpressionRoot(self, ctx:GrammarParser.ExpressionRootContext):
        pass

    # Exit a parse tree produced by GrammarParser#expressionRoot.
    def exitExpressionRoot(self, ctx:GrammarParser.ExpressionRootContext):
        pass


    # Enter a parse tree produced by GrammarParser#modExpr.
    def enterModExpr(self, ctx:GrammarParser.ModExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#modExpr.
    def exitModExpr(self, ctx:GrammarParser.ModExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#mmaxExpr.
    def enterMmaxExpr(self, ctx:GrammarParser.MmaxExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#mmaxExpr.
    def exitMmaxExpr(self, ctx:GrammarParser.MmaxExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#numberExpr.
    def enterNumberExpr(self, ctx:GrammarParser.NumberExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#numberExpr.
    def exitNumberExpr(self, ctx:GrammarParser.NumberExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#subExpr.
    def enterSubExpr(self, ctx:GrammarParser.SubExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#subExpr.
    def exitSubExpr(self, ctx:GrammarParser.SubExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#minusExpr.
    def enterMinusExpr(self, ctx:GrammarParser.MinusExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#minusExpr.
    def exitMinusExpr(self, ctx:GrammarParser.MinusExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#multExpr.
    def enterMultExpr(self, ctx:GrammarParser.MultExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#multExpr.
    def exitMultExpr(self, ctx:GrammarParser.MultExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#parenExpr.
    def enterParenExpr(self, ctx:GrammarParser.ParenExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#parenExpr.
    def exitParenExpr(self, ctx:GrammarParser.ParenExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#plusExpr.
    def enterPlusExpr(self, ctx:GrammarParser.PlusExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#plusExpr.
    def exitPlusExpr(self, ctx:GrammarParser.PlusExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#addExpr.
    def enterAddExpr(self, ctx:GrammarParser.AddExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#addExpr.
    def exitAddExpr(self, ctx:GrammarParser.AddExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#mminExpr.
    def enterMminExpr(self, ctx:GrammarParser.MminExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#mminExpr.
    def exitMminExpr(self, ctx:GrammarParser.MminExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#cellRefExpr.
    def enterCellRefExpr(self, ctx:GrammarParser.CellRefExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#cellRefExpr.
    def exitCellRefExpr(self, ctx:GrammarParser.CellRefExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#divExpr.
    def enterDivExpr(self, ctx:GrammarParser.DivExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#divExpr.
    def exitDivExpr(self, ctx:GrammarParser.DivExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#divFuncExpr.
    def enterDivFuncExpr(self, ctx:GrammarParser.DivFuncExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#divFuncExpr.
    def exitDivFuncExpr(self, ctx:GrammarParser.DivFuncExprContext):
        pass



del GrammarParser