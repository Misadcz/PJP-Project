# Generated from Expr.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#par.
    def visitPar(self, ctx:ExprParser.ParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#add.
    def visitAdd(self, ctx:ExprParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#oct.
    def visitOct(self, ctx:ExprParser.OctContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mul.
    def visitMul(self, ctx:ExprParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#hexa.
    def visitHexa(self, ctx:ExprParser.HexaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#int.
    def visitInt(self, ctx:ExprParser.IntContext):
        return self.visitChildren(ctx)



del ExprParser