# Generated from Expr.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,12,73,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,1,1,
        1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,4,7,41,8,7,11,7,12,
        7,42,1,8,1,8,5,8,47,8,8,10,8,12,8,50,9,8,1,9,1,9,5,9,54,8,9,10,9,
        12,9,57,9,9,1,10,1,10,1,10,1,10,4,10,63,8,10,11,10,12,10,64,1,11,
        4,11,68,8,11,11,11,12,11,69,1,11,1,11,0,0,12,1,1,3,2,5,3,7,4,9,5,
        11,6,13,7,15,8,17,9,19,10,21,11,23,12,1,0,6,2,0,65,90,97,122,1,0,
        49,57,1,0,48,57,1,0,48,55,3,0,48,57,65,70,97,102,3,0,9,10,13,13,
        32,32,77,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,
        0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,
        0,0,0,21,1,0,0,0,0,23,1,0,0,0,1,25,1,0,0,0,3,27,1,0,0,0,5,29,1,0,
        0,0,7,31,1,0,0,0,9,33,1,0,0,0,11,35,1,0,0,0,13,37,1,0,0,0,15,40,
        1,0,0,0,17,44,1,0,0,0,19,51,1,0,0,0,21,58,1,0,0,0,23,67,1,0,0,0,
        25,26,5,59,0,0,26,2,1,0,0,0,27,28,5,42,0,0,28,4,1,0,0,0,29,30,5,
        47,0,0,30,6,1,0,0,0,31,32,5,43,0,0,32,8,1,0,0,0,33,34,5,45,0,0,34,
        10,1,0,0,0,35,36,5,40,0,0,36,12,1,0,0,0,37,38,5,41,0,0,38,14,1,0,
        0,0,39,41,7,0,0,0,40,39,1,0,0,0,41,42,1,0,0,0,42,40,1,0,0,0,42,43,
        1,0,0,0,43,16,1,0,0,0,44,48,7,1,0,0,45,47,7,2,0,0,46,45,1,0,0,0,
        47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,18,1,0,0,0,50,48,1,
        0,0,0,51,55,5,48,0,0,52,54,7,3,0,0,53,52,1,0,0,0,54,57,1,0,0,0,55,
        53,1,0,0,0,55,56,1,0,0,0,56,20,1,0,0,0,57,55,1,0,0,0,58,59,5,48,
        0,0,59,60,5,120,0,0,60,62,1,0,0,0,61,63,7,4,0,0,62,61,1,0,0,0,63,
        64,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,22,1,0,0,0,66,68,7,5,0,
        0,67,66,1,0,0,0,68,69,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,71,
        1,0,0,0,71,72,6,11,0,0,72,24,1,0,0,0,6,0,42,48,55,64,69,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    ID = 8
    INT = 9
    OCT = 10
    HEXA = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'*'", "'/'", "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "OCT", "HEXA", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "ID", "INT", "OCT", "HEXA", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


