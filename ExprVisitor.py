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


    # Visit a parse tree produced by ExprParser#type.
    def visitType(self, ctx:ExprParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#id.
    def visitId(self, ctx:ExprParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#int.
    def visitInt(self, ctx:ExprParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#float.
    def visitFloat(self, ctx:ExprParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#string.
    def visitString(self, ctx:ExprParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bool.
    def visitBool(self, ctx:ExprParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#empty.
    def visitEmpty(self, ctx:ExprParser.EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#declaration.
    def visitDeclaration(self, ctx:ExprParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx:ExprParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#read.
    def visitRead(self, ctx:ExprParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#write.
    def visitWrite(self, ctx:ExprParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#block.
    def visitBlock(self, ctx:ExprParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#if.
    def visitIf(self, ctx:ExprParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#while.
    def visitWhile(self, ctx:ExprParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#for.
    def visitFor(self, ctx:ExprParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#compare.
    def visitCompare(self, ctx:ExprParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#or.
    def visitOr(self, ctx:ExprParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#var.
    def visitVar(self, ctx:ExprParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignment.
    def visitAssignment(self, ctx:ExprParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#equalnotequal.
    def visitEqualnotequal(self, ctx:ExprParser.EqualnotequalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#addSub.
    def visitAddSub(self, ctx:ExprParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parenthesis.
    def visitParenthesis(self, ctx:ExprParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mulDiv.
    def visitMulDiv(self, ctx:ExprParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#not.
    def visitNot(self, ctx:ExprParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#lit.
    def visitLit(self, ctx:ExprParser.LitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#and.
    def visitAnd(self, ctx:ExprParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#unaryminus.
    def visitUnaryminus(self, ctx:ExprParser.UnaryminusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ternary.
    def visitTernary(self, ctx:ExprParser.TernaryContext):
        return self.visitChildren(ctx)



del ExprParser