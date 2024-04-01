import sys
from antlr4 import *
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

class VisitorInterp(ExprVisitor):

        def visitInt(self, ctx:ExprParser.IntContext):
            return int(ctx.INT().getText(),10)
        
        def visitHexa(self, ctx:ExprParser.HexaContext):
            return int(ctx.HEXA().getText(), 16)
        
        def visitOct(self, ctx:ExprParser.OctContext):
            return int(ctx.OCT().getText(), 8)
        
        def visitPar(self, ctx: ExprParser.ParContext):
            return self.visit(ctx.expr())
         
        def visitAdd(self, ctx: ExprParser.AddContext):
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            if ctx.op.text == '+':
                return left + right
            else:
                return left - right
        
        def visitMul(self, ctx: ExprParser.MulContext):
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            if ctx.op.text == '*':
                return left * right
            else:
                return left // right
            
        def visitProg(self, ctx: ExprParser.ProgContext):
            for i in range(ctx.getChildCount()):
                if(self.visit(ctx.getChild(i))) or (self.visit(ctx.getChild(i)) == 0):
                    print(self.visit(ctx.getChild(i)))
            return ''
        