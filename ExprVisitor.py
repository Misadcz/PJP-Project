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


    # Visit a parse tree produced by ExprParser#ifStatement.
    def visitIfStatement(self, ctx:ExprParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#writeStatement.
    def visitWriteStatement(self, ctx:ExprParser.WriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#readStatement.
    def visitReadStatement(self, ctx:ExprParser.ReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#forStatement.
    def visitForStatement(self, ctx:ExprParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:ExprParser.DoWhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#whileStatement.
    def visitWhileStatement(self, ctx:ExprParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#block.
    def visitBlock(self, ctx:ExprParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#statement.
    def visitStatement(self, ctx:ExprParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#cond.
    def visitCond(self, ctx:ExprParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#comp.
    def visitComp(self, ctx:ExprParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignStatement.
    def visitAssignStatement(self, ctx:ExprParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#operationStatement.
    def visitOperationStatement(self, ctx:ExprParser.OperationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#variable.
    def visitVariable(self, ctx:ExprParser.VariableContext):
        return self.visitChildren(ctx)



del ExprParser