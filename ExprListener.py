# Generated from Expr.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        for i in range(ctx.getChildCount()):
            print(self.visit(ctx.getChild(i)))

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#par.
    def enterPar(self, ctx:ExprParser.ParContext):
        pass

    # Exit a parse tree produced by ExprParser#par.
    def exitPar(self, ctx:ExprParser.ParContext):
        return self.visit(ctx.expr())


    # Enter a parse tree produced by ExprParser#add.
    def enterAdd(self, ctx:ExprParser.AddContext):
        pass

    # Exit a parse tree produced by ExprParser#add.
    def exitAdd(self, ctx:ExprParser.AddContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '+':
            return left + right
        else:
            return left - right
       

    # Enter a parse tree produced by ExprParser#oct.
    def enterOct(self, ctx:ExprParser.OctContext):
        pass

    # Exit a parse tree produced by ExprParser#oct.
    def exitOct(self, ctx:ExprParser.OctContext):
        return int(ctx.OCT().getText(), 8)


    # Enter a parse tree produced by ExprParser#mul.
    def enterMul(self, ctx:ExprParser.MulContext):
        pass

    # Exit a parse tree produced by ExprParser#mul.
    def exitMul(self, ctx:ExprParser.MulContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '*':
            return left * right
        else:
            return left // right


    # Enter a parse tree produced by ExprParser#hexa.
    def enterHexa(self, ctx:ExprParser.HexaContext):
        pass

    # Exit a parse tree produced by ExprParser#hexa.
    def exitHexa(self, ctx:ExprParser.HexaContext):
        return int(ctx.HEXA().getText(), 16)


    # Enter a parse tree produced by ExprParser#int.
    def enterInt(self, ctx:ExprParser.IntContext):
        pass

    # Exit a parse tree produced by ExprParser#int.
    def exitInt(self, ctx:ExprParser.IntContext):
        return int(ctx.INT().getText())



del ExprParser