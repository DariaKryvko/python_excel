# Generated from Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#expressionRoot.
    def visitExpressionRoot(self, ctx:GrammarParser.ExpressionRootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#modExpr.
    def visitModExpr(self, ctx:GrammarParser.ModExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#mmaxExpr.
    def visitMmaxExpr(self, ctx:GrammarParser.MmaxExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#numberExpr.
    def visitNumberExpr(self, ctx:GrammarParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#subExpr.
    def visitSubExpr(self, ctx:GrammarParser.SubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#minusExpr.
    def visitMinusExpr(self, ctx:GrammarParser.MinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#multExpr.
    def visitMultExpr(self, ctx:GrammarParser.MultExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#parenExpr.
    def visitParenExpr(self, ctx:GrammarParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#plusExpr.
    def visitPlusExpr(self, ctx:GrammarParser.PlusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#addExpr.
    def visitAddExpr(self, ctx:GrammarParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#mminExpr.
    def visitMminExpr(self, ctx:GrammarParser.MminExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#cellRefExpr.
    def visitCellRefExpr(self, ctx:GrammarParser.CellRefExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#divExpr.
    def visitDivExpr(self, ctx:GrammarParser.DivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#divFuncExpr.
    def visitDivFuncExpr(self, ctx:GrammarParser.DivFuncExprContext):
        return self.visitChildren(ctx)



del GrammarParser