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
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#ifStatement.
    def enterIfStatement(self, ctx:ExprParser.IfStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#ifStatement.
    def exitIfStatement(self, ctx:ExprParser.IfStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#writeStatement.
    def enterWriteStatement(self, ctx:ExprParser.WriteStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#writeStatement.
    def exitWriteStatement(self, ctx:ExprParser.WriteStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#readStatement.
    def enterReadStatement(self, ctx:ExprParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#readStatement.
    def exitReadStatement(self, ctx:ExprParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#forStatement.
    def enterForStatement(self, ctx:ExprParser.ForStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#forStatement.
    def exitForStatement(self, ctx:ExprParser.ForStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:ExprParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:ExprParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#whileStatement.
    def enterWhileStatement(self, ctx:ExprParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#whileStatement.
    def exitWhileStatement(self, ctx:ExprParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#block.
    def enterBlock(self, ctx:ExprParser.BlockContext):
        pass

    # Exit a parse tree produced by ExprParser#block.
    def exitBlock(self, ctx:ExprParser.BlockContext):
        pass


    # Enter a parse tree produced by ExprParser#statement.
    def enterStatement(self, ctx:ExprParser.StatementContext):
        pass

    # Exit a parse tree produced by ExprParser#statement.
    def exitStatement(self, ctx:ExprParser.StatementContext):
        pass


    # Enter a parse tree produced by ExprParser#cond.
    def enterCond(self, ctx:ExprParser.CondContext):
        pass

    # Exit a parse tree produced by ExprParser#cond.
    def exitCond(self, ctx:ExprParser.CondContext):
        pass


    # Enter a parse tree produced by ExprParser#comp.
    def enterComp(self, ctx:ExprParser.CompContext):
        pass

    # Exit a parse tree produced by ExprParser#comp.
    def exitComp(self, ctx:ExprParser.CompContext):
        pass


    # Enter a parse tree produced by ExprParser#assignStatement.
    def enterAssignStatement(self, ctx:ExprParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#assignStatement.
    def exitAssignStatement(self, ctx:ExprParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#operationStatement.
    def enterOperationStatement(self, ctx:ExprParser.OperationStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#operationStatement.
    def exitOperationStatement(self, ctx:ExprParser.OperationStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#variable.
    def enterVariable(self, ctx:ExprParser.VariableContext):
        pass

    # Exit a parse tree produced by ExprParser#variable.
    def exitVariable(self, ctx:ExprParser.VariableContext):
        pass



del ExprParser