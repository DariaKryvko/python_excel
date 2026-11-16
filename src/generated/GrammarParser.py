# Generated from Grammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,68,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,5,1,18,8,1,10,1,12,1,21,9,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,5,1,30,8,1,10,1,12,1,33,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,43,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,5,1,63,8,1,10,1,12,1,66,9,1,1,1,0,1,2,2,0,2,
        0,0,79,0,4,1,0,0,0,2,42,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,
        0,0,7,8,6,1,-1,0,8,9,5,1,0,0,9,10,3,2,1,0,10,11,5,2,0,0,11,43,1,
        0,0,0,12,13,5,8,0,0,13,14,5,1,0,0,14,19,3,2,1,0,15,16,5,3,0,0,16,
        18,3,2,1,0,17,15,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,
        0,20,22,1,0,0,0,21,19,1,0,0,0,22,23,5,2,0,0,23,43,1,0,0,0,24,25,
        5,9,0,0,25,26,5,1,0,0,26,31,3,2,1,0,27,28,5,3,0,0,28,30,3,2,1,0,
        29,27,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,34,1,
        0,0,0,33,31,1,0,0,0,34,35,5,2,0,0,35,43,1,0,0,0,36,43,5,12,0,0,37,
        38,5,4,0,0,38,43,3,2,1,9,39,40,5,5,0,0,40,43,3,2,1,8,41,43,5,13,
        0,0,42,7,1,0,0,0,42,12,1,0,0,0,42,24,1,0,0,0,42,36,1,0,0,0,42,37,
        1,0,0,0,42,39,1,0,0,0,42,41,1,0,0,0,43,64,1,0,0,0,44,45,10,7,0,0,
        45,46,5,6,0,0,46,63,3,2,1,8,47,48,10,6,0,0,48,49,5,7,0,0,49,63,3,
        2,1,7,50,51,10,5,0,0,51,52,5,10,0,0,52,63,3,2,1,6,53,54,10,4,0,0,
        54,55,5,11,0,0,55,63,3,2,1,5,56,57,10,3,0,0,57,58,5,4,0,0,58,63,
        3,2,1,4,59,60,10,2,0,0,60,61,5,5,0,0,61,63,3,2,1,3,62,44,1,0,0,0,
        62,47,1,0,0,0,62,50,1,0,0,0,62,53,1,0,0,0,62,56,1,0,0,0,62,59,1,
        0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,3,1,0,0,0,66,
        64,1,0,0,0,5,19,31,42,62,64
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "'+'", "'-'", "'*'", 
                     "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "MMAX", "MMIN", "DIV", "MOD", "CELL", "INT", "WS" ]

    RULE_expressionRoot = 0
    RULE_expression = 1

    ruleNames =  [ "expressionRoot", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    MMAX=8
    MMIN=9
    DIV=10
    MOD=11
    CELL=12
    INT=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionRootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def EOF(self):
            return self.getToken(GrammarParser.EOF, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_expressionRoot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionRoot" ):
                listener.enterExpressionRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionRoot" ):
                listener.exitExpressionRoot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionRoot" ):
                return visitor.visitExpressionRoot(self)
            else:
                return visitor.visitChildren(self)




    def expressionRoot(self):

        localctx = GrammarParser.ExpressionRootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expressionRoot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expression(0)
            self.state = 5
            self.match(GrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ModExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)

        def MOD(self):
            return self.getToken(GrammarParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModExpr" ):
                listener.enterModExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModExpr" ):
                listener.exitModExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModExpr" ):
                return visitor.visitModExpr(self)
            else:
                return visitor.visitChildren(self)


    class MmaxExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MMAX(self):
            return self.getToken(GrammarParser.MMAX, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMmaxExpr" ):
                listener.enterMmaxExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMmaxExpr" ):
                listener.exitMmaxExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMmaxExpr" ):
                return visitor.visitMmaxExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(GrammarParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class SubExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubExpr" ):
                listener.enterSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubExpr" ):
                listener.exitSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubExpr" ):
                return visitor.visitSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class MinusExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinusExpr" ):
                listener.enterMinusExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinusExpr" ):
                listener.exitMinusExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinusExpr" ):
                return visitor.visitMinusExpr(self)
            else:
                return visitor.visitChildren(self)


    class MultExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultExpr" ):
                listener.enterMultExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultExpr" ):
                listener.exitMultExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultExpr" ):
                return visitor.visitMultExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class PlusExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlusExpr" ):
                listener.enterPlusExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlusExpr" ):
                listener.exitPlusExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlusExpr" ):
                return visitor.visitPlusExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)


    class MminExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MMIN(self):
            return self.getToken(GrammarParser.MMIN, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMminExpr" ):
                listener.enterMminExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMminExpr" ):
                listener.exitMminExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMminExpr" ):
                return visitor.visitMminExpr(self)
            else:
                return visitor.visitChildren(self)


    class CellRefExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CELL(self):
            return self.getToken(GrammarParser.CELL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCellRefExpr" ):
                listener.enterCellRefExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCellRefExpr" ):
                listener.exitCellRefExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCellRefExpr" ):
                return visitor.visitCellRefExpr(self)
            else:
                return visitor.visitChildren(self)


    class DivExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivExpr" ):
                listener.enterDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivExpr" ):
                listener.exitDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivExpr" ):
                return visitor.visitDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class DivFuncExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)

        def DIV(self):
            return self.getToken(GrammarParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivFuncExpr" ):
                listener.enterDivFuncExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivFuncExpr" ):
                listener.exitDivFuncExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivFuncExpr" ):
                return visitor.visitDivFuncExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = GrammarParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 8
                self.match(GrammarParser.T__0)
                self.state = 9
                self.expression(0)
                self.state = 10
                self.match(GrammarParser.T__1)
                pass
            elif token in [8]:
                localctx = GrammarParser.MmaxExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                self.match(GrammarParser.MMAX)
                self.state = 13
                self.match(GrammarParser.T__0)
                self.state = 14
                self.expression(0)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 15
                    self.match(GrammarParser.T__2)
                    self.state = 16
                    self.expression(0)
                    self.state = 21
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 22
                self.match(GrammarParser.T__1)
                pass
            elif token in [9]:
                localctx = GrammarParser.MminExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(GrammarParser.MMIN)
                self.state = 25
                self.match(GrammarParser.T__0)
                self.state = 26
                self.expression(0)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 27
                    self.match(GrammarParser.T__2)
                    self.state = 28
                    self.expression(0)
                    self.state = 33
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 34
                self.match(GrammarParser.T__1)
                pass
            elif token in [12]:
                localctx = GrammarParser.CellRefExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 36
                self.match(GrammarParser.CELL)
                pass
            elif token in [4]:
                localctx = GrammarParser.PlusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 37
                self.match(GrammarParser.T__3)
                self.state = 38
                self.expression(9)
                pass
            elif token in [5]:
                localctx = GrammarParser.MinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                self.match(GrammarParser.T__4)
                self.state = 40
                self.expression(8)
                pass
            elif token in [13]:
                localctx = GrammarParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 41
                self.match(GrammarParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 62
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.MultExprContext(self, GrammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 44
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 45
                        self.match(GrammarParser.T__5)
                        self.state = 46
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.DivExprContext(self, GrammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 47
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 48
                        self.match(GrammarParser.T__6)
                        self.state = 49
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.DivFuncExprContext(self, GrammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 50
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 51
                        self.match(GrammarParser.DIV)
                        self.state = 52
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.ModExprContext(self, GrammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 53
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 54
                        self.match(GrammarParser.MOD)
                        self.state = 55
                        self.expression(5)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.AddExprContext(self, GrammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 56
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 57
                        self.match(GrammarParser.T__3)
                        self.state = 58
                        self.expression(4)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.SubExprContext(self, GrammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 59
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 60
                        self.match(GrammarParser.T__4)
                        self.state = 61
                        self.expression(3)
                        pass

             
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




