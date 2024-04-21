# Generated from Expr.g4 by ANTLR 4.13.0
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
        4,1,39,146,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,3,3,26,8,3,
        1,4,1,4,1,4,1,4,1,4,5,4,33,8,4,10,4,12,4,36,9,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,5,4,47,8,4,10,4,12,4,50,9,4,1,4,1,4,1,4,1,4,
        1,4,1,4,5,4,58,8,4,10,4,12,4,61,9,4,1,4,1,4,1,4,1,4,5,4,67,8,4,10,
        4,12,4,70,9,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,80,8,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,98,8,
        4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,
        5,115,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,141,8,5,10,5,12,5,
        144,9,5,1,5,0,1,10,6,0,2,4,6,8,10,0,5,1,0,1,4,1,0,24,25,1,0,26,27,
        2,0,19,19,22,23,2,0,15,15,20,21,168,0,13,1,0,0,0,2,17,1,0,0,0,4,
        19,1,0,0,0,6,25,1,0,0,0,8,97,1,0,0,0,10,114,1,0,0,0,12,14,3,8,4,
        0,13,12,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,1,1,
        0,0,0,17,18,7,0,0,0,18,3,1,0,0,0,19,20,5,33,0,0,20,5,1,0,0,0,21,
        26,5,34,0,0,22,26,5,35,0,0,23,26,5,36,0,0,24,26,5,37,0,0,25,21,1,
        0,0,0,25,22,1,0,0,0,25,23,1,0,0,0,25,24,1,0,0,0,26,7,1,0,0,0,27,
        98,5,31,0,0,28,29,3,2,1,0,29,34,3,4,2,0,30,31,5,32,0,0,31,33,3,4,
        2,0,32,30,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,37,
        1,0,0,0,36,34,1,0,0,0,37,38,5,31,0,0,38,98,1,0,0,0,39,40,3,10,5,
        0,40,41,5,31,0,0,41,98,1,0,0,0,42,43,5,5,0,0,43,48,3,4,2,0,44,45,
        5,32,0,0,45,47,3,4,2,0,46,44,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,
        48,49,1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,0,51,52,5,31,0,0,52,98,1,
        0,0,0,53,54,5,6,0,0,54,59,3,10,5,0,55,56,5,32,0,0,56,58,3,10,5,0,
        57,55,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,62,1,
        0,0,0,61,59,1,0,0,0,62,63,5,31,0,0,63,98,1,0,0,0,64,68,5,7,0,0,65,
        67,3,8,4,0,66,65,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,
        0,69,71,1,0,0,0,70,68,1,0,0,0,71,98,5,8,0,0,72,73,5,9,0,0,73,74,
        5,10,0,0,74,75,3,10,5,0,75,76,5,11,0,0,76,79,3,8,4,0,77,78,5,12,
        0,0,78,80,3,8,4,0,79,77,1,0,0,0,79,80,1,0,0,0,80,98,1,0,0,0,81,82,
        5,13,0,0,82,83,5,10,0,0,83,84,3,10,5,0,84,85,5,11,0,0,85,86,3,8,
        4,0,86,98,1,0,0,0,87,88,5,14,0,0,88,89,5,10,0,0,89,90,3,10,5,0,90,
        91,5,31,0,0,91,92,3,10,5,0,92,93,5,31,0,0,93,94,3,10,5,0,94,95,5,
        11,0,0,95,96,3,8,4,0,96,98,1,0,0,0,97,27,1,0,0,0,97,28,1,0,0,0,97,
        39,1,0,0,0,97,42,1,0,0,0,97,53,1,0,0,0,97,64,1,0,0,0,97,72,1,0,0,
        0,97,81,1,0,0,0,97,87,1,0,0,0,98,9,1,0,0,0,99,100,6,5,-1,0,100,115,
        3,6,3,0,101,115,3,4,2,0,102,103,3,4,2,0,103,104,5,16,0,0,104,105,
        3,10,5,5,105,115,1,0,0,0,106,107,5,30,0,0,107,115,3,10,5,4,108,109,
        5,10,0,0,109,110,3,10,5,0,110,111,5,11,0,0,111,115,1,0,0,0,112,113,
        5,21,0,0,113,115,3,10,5,2,114,99,1,0,0,0,114,101,1,0,0,0,114,102,
        1,0,0,0,114,106,1,0,0,0,114,108,1,0,0,0,114,112,1,0,0,0,115,142,
        1,0,0,0,116,117,10,11,0,0,117,118,5,28,0,0,118,141,3,10,5,12,119,
        120,10,10,0,0,120,121,5,29,0,0,121,141,3,10,5,11,122,123,10,9,0,
        0,123,124,7,1,0,0,124,141,3,10,5,10,125,126,10,8,0,0,126,127,7,2,
        0,0,127,141,3,10,5,9,128,129,10,7,0,0,129,130,7,3,0,0,130,141,3,
        10,5,8,131,132,10,6,0,0,132,133,7,4,0,0,133,141,3,10,5,7,134,135,
        10,1,0,0,135,136,5,17,0,0,136,137,3,10,5,0,137,138,5,18,0,0,138,
        139,3,10,5,2,139,141,1,0,0,0,140,116,1,0,0,0,140,119,1,0,0,0,140,
        122,1,0,0,0,140,125,1,0,0,0,140,128,1,0,0,0,140,131,1,0,0,0,140,
        134,1,0,0,0,141,144,1,0,0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,
        11,1,0,0,0,144,142,1,0,0,0,11,15,25,34,48,59,68,79,97,114,140,142
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'string'", "'bool'", 
                     "'read'", "'write'", "'{'", "'}'", "'if'", "'('", "')'", 
                     "'else'", "'while'", "'for'", "'.'", "'='", "'?'", 
                     "':'", "'%'", "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", 
                     "'<'", "'>'", "'&&'", "'||'", "'!'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "MOD", "PLUS", 
                      "MINUS", "MULT", "DIV", "EQUAL", "NOTEQUAL", "LESSTHAN", 
                      "GREATERTHAN", "AND", "OR", "NOT", "SEMICOLON", "COMMA", 
                      "ID", "INT", "FLOAT", "STRING", "BOOL", "WS", "COMMENT" ]

    RULE_prog = 0
    RULE_type = 1
    RULE_variable = 2
    RULE_literal = 3
    RULE_statement = 4
    RULE_expression = 5

    ruleNames =  [ "prog", "type", "variable", "literal", "statement", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    MOD=19
    PLUS=20
    MINUS=21
    MULT=22
    DIV=23
    EQUAL=24
    NOTEQUAL=25
    LESSTHAN=26
    GREATERTHAN=27
    AND=28
    OR=29
    NOT=30
    SEMICOLON=31
    COMMA=32
    ID=33
    INT=34
    FLOAT=35
    STRING=36
    BOOL=37
    WS=38
    COMMENT=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.statement()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 269511321342) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = ExprParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_variable

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IdContext(VariableContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.VariableContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)



    def variable(self):

        localctx = ExprParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable)
        try:
            localctx = ExprParser.IdContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(ExprParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class BoolContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(ExprParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(ExprParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = ExprParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_literal)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                localctx = ExprParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.match(ExprParser.INT)
                pass
            elif token in [35]:
                localctx = ExprParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.match(ExprParser.FLOAT)
                pass
            elif token in [36]:
                localctx = ExprParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.match(ExprParser.STRING)
                pass
            elif token in [37]:
                localctx = ExprParser.BoolContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.match(ExprParser.BOOL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReadContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.VariableContext)
            else:
                return self.getTypedRuleContext(ExprParser.VariableContext,i)

        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)


    class ForContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.SEMICOLON)
            else:
                return self.getToken(ExprParser.SEMICOLON, i)
        def statement(self):
            return self.getTypedRuleContext(ExprParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor" ):
                listener.enterFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor" ):
                listener.exitFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor" ):
                return visitor.visitFor(self)
            else:
                return visitor.visitChildren(self)


    class ExprContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)

        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)


    class BlockContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)

        def statement(self):
            return self.getTypedRuleContext(ExprParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class DeclarationContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(ExprParser.TypeContext,0)

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.VariableContext)
            else:
                return self.getTypedRuleContext(ExprParser.VariableContext,i)

        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class WriteContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)

        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class EmptyContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmpty" ):
                listener.enterEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmpty" ):
                listener.exitEmpty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmpty" ):
                return visitor.visitEmpty(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                localctx = ExprParser.EmptyContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(ExprParser.SEMICOLON)
                pass
            elif token in [1, 2, 3, 4]:
                localctx = ExprParser.DeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.type_()
                self.state = 29
                self.variable()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==32:
                    self.state = 30
                    self.match(ExprParser.COMMA)
                    self.state = 31
                    self.variable()
                    self.state = 36
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 37
                self.match(ExprParser.SEMICOLON)
                pass
            elif token in [10, 21, 30, 33, 34, 35, 36, 37]:
                localctx = ExprParser.ExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.expression(0)
                self.state = 40
                self.match(ExprParser.SEMICOLON)
                pass
            elif token in [5]:
                localctx = ExprParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.match(ExprParser.T__4)
                self.state = 43
                self.variable()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==32:
                    self.state = 44
                    self.match(ExprParser.COMMA)
                    self.state = 45
                    self.variable()
                    self.state = 50
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 51
                self.match(ExprParser.SEMICOLON)
                pass
            elif token in [6]:
                localctx = ExprParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 53
                self.match(ExprParser.T__5)
                self.state = 54
                self.expression(0)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==32:
                    self.state = 55
                    self.match(ExprParser.COMMA)
                    self.state = 56
                    self.expression(0)
                    self.state = 61
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 62
                self.match(ExprParser.SEMICOLON)
                pass
            elif token in [7]:
                localctx = ExprParser.BlockContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 64
                self.match(ExprParser.T__6)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 269511321342) != 0):
                    self.state = 65
                    self.statement()
                    self.state = 70
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 71
                self.match(ExprParser.T__7)
                pass
            elif token in [9]:
                localctx = ExprParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 72
                self.match(ExprParser.T__8)
                self.state = 73
                self.match(ExprParser.T__9)
                self.state = 74
                self.expression(0)
                self.state = 75
                self.match(ExprParser.T__10)
                self.state = 76
                self.statement()
                self.state = 79
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 77
                    self.match(ExprParser.T__11)
                    self.state = 78
                    self.statement()


                pass
            elif token in [13]:
                localctx = ExprParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 81
                self.match(ExprParser.T__12)
                self.state = 82
                self.match(ExprParser.T__9)
                self.state = 83
                self.expression(0)
                self.state = 84
                self.match(ExprParser.T__10)

                self.state = 85
                self.statement()
                pass
            elif token in [14]:
                localctx = ExprParser.ForContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 87
                self.match(ExprParser.T__13)
                self.state = 88
                self.match(ExprParser.T__9)
                self.state = 89
                self.expression(0)
                self.state = 90
                self.match(ExprParser.SEMICOLON)
                self.state = 91
                self.expression(0)
                self.state = 92
                self.match(ExprParser.SEMICOLON)
                self.state = 93
                self.expression(0)
                self.state = 94
                self.match(ExprParser.T__10)

                self.state = 95
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

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
            return ExprParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class CompareContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)

        def LESSTHAN(self):
            return self.getToken(ExprParser.LESSTHAN, 0)
        def GREATERTHAN(self):
            return self.getToken(ExprParser.GREATERTHAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompare" ):
                listener.enterCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompare" ):
                listener.exitCompare(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare" ):
                return visitor.visitCompare(self)
            else:
                return visitor.visitChildren(self)


    class OrContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)

        def OR(self):
            return self.getToken(ExprParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(ExprParser.VariableContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(ExprParser.VariableContext,0)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)


    class EqualnotequalContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)

        def EQUAL(self):
            return self.getToken(ExprParser.EQUAL, 0)
        def NOTEQUAL(self):
            return self.getToken(ExprParser.NOTEQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualnotequal" ):
                listener.enterEqualnotequal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualnotequal" ):
                listener.exitEqualnotequal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualnotequal" ):
                return visitor.visitEqualnotequal(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(ExprParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(ExprParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesis" ):
                listener.enterParenthesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesis" ):
                listener.exitParenthesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)

        def MULT(self):
            return self.getToken(ExprParser.MULT, 0)
        def DIV(self):
            return self.getToken(ExprParser.DIV, 0)
        def MOD(self):
            return self.getToken(ExprParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class NotContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(ExprParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot" ):
                listener.enterNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot" ):
                listener.exitNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot" ):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


    class LitContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(ExprParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLit" ):
                listener.enterLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLit" ):
                listener.exitLit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit" ):
                return visitor.visitLit(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)

        def AND(self):
            return self.getToken(ExprParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class UnaryminusContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(ExprParser.MINUS, 0)
        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryminus" ):
                listener.enterUnaryminus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryminus" ):
                listener.exitUnaryminus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryminus" ):
                return visitor.visitUnaryminus(self)
            else:
                return visitor.visitChildren(self)


    class TernaryContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTernary" ):
                listener.enterTernary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTernary" ):
                listener.exitTernary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTernary" ):
                return visitor.visitTernary(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = ExprParser.LitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 100
                self.literal()
                pass

            elif la_ == 2:
                localctx = ExprParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 101
                self.variable()
                pass

            elif la_ == 3:
                localctx = ExprParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 102
                self.variable()
                self.state = 103
                self.match(ExprParser.T__15)
                self.state = 104
                self.expression(5)
                pass

            elif la_ == 4:
                localctx = ExprParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.match(ExprParser.NOT)
                self.state = 107
                self.expression(4)
                pass

            elif la_ == 5:
                localctx = ExprParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 108
                self.match(ExprParser.T__9)
                self.state = 109
                self.expression(0)
                self.state = 110
                self.match(ExprParser.T__10)
                pass

            elif la_ == 6:
                localctx = ExprParser.UnaryminusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 112
                self.match(ExprParser.MINUS)
                self.state = 113
                self.expression(2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 142
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 140
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.AndContext(self, ExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 116
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 117
                        self.match(ExprParser.AND)
                        self.state = 118
                        self.expression(12)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.OrContext(self, ExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 119
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 120
                        self.match(ExprParser.OR)
                        self.state = 121
                        self.expression(11)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.EqualnotequalContext(self, ExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 122
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 123
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==24 or _la==25):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 124
                        self.expression(10)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.CompareContext(self, ExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 125
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 126
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 127
                        self.expression(9)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.MulDivContext(self, ExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 128
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 129
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 13107200) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 130
                        self.expression(8)
                        pass

                    elif la_ == 6:
                        localctx = ExprParser.AddSubContext(self, ExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 131
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 132
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3178496) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 133
                        self.expression(7)
                        pass

                    elif la_ == 7:
                        localctx = ExprParser.TernaryContext(self, ExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 134
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 135
                        self.match(ExprParser.T__16)
                        self.state = 136
                        self.expression(0)
                        self.state = 137
                        self.match(ExprParser.T__17)
                        self.state = 138
                        self.expression(2)
                        pass

             
                self.state = 144
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        self._predicates[5] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         




