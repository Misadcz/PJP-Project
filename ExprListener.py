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


    # Enter a parse tree produced by ExprParser#type.
    def enterType(self, ctx:ExprParser.TypeContext):
        pass

    # Exit a parse tree produced by ExprParser#type.
    def exitType(self, ctx:ExprParser.TypeContext):
        pass


    # Enter a parse tree produced by ExprParser#id.
    def enterId(self, ctx:ExprParser.IdContext):
        pass

    # Exit a parse tree produced by ExprParser#id.
    def exitId(self, ctx:ExprParser.IdContext):
        pass


    # Enter a parse tree produced by ExprParser#int.
    def enterInt(self, ctx:ExprParser.IntContext):
        pass

    # Exit a parse tree produced by ExprParser#int.
    def exitInt(self, ctx:ExprParser.IntContext):
        pass


    # Enter a parse tree produced by ExprParser#float.
    def enterFloat(self, ctx:ExprParser.FloatContext):
        pass

    # Exit a parse tree produced by ExprParser#float.
    def exitFloat(self, ctx:ExprParser.FloatContext):
        pass


    # Enter a parse tree produced by ExprParser#string.
    def enterString(self, ctx:ExprParser.StringContext):
        pass

    # Exit a parse tree produced by ExprParser#string.
    def exitString(self, ctx:ExprParser.StringContext):
        pass


    # Enter a parse tree produced by ExprParser#bool.
    def enterBool(self, ctx:ExprParser.BoolContext):
        pass

    # Exit a parse tree produced by ExprParser#bool.
    def exitBool(self, ctx:ExprParser.BoolContext):
        pass


    # Enter a parse tree produced by ExprParser#empty.
    def enterEmpty(self, ctx:ExprParser.EmptyContext):
        pass

    # Exit a parse tree produced by ExprParser#empty.
    def exitEmpty(self, ctx:ExprParser.EmptyContext):
        pass


    # Enter a parse tree produced by ExprParser#declaration.
    def enterDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#declaration.
    def exitDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#read.
    def enterRead(self, ctx:ExprParser.ReadContext):
        pass

    # Exit a parse tree produced by ExprParser#read.
    def exitRead(self, ctx:ExprParser.ReadContext):
        pass


    # Enter a parse tree produced by ExprParser#write.
    def enterWrite(self, ctx:ExprParser.WriteContext):
        pass

    # Exit a parse tree produced by ExprParser#write.
    def exitWrite(self, ctx:ExprParser.WriteContext):
        pass


    # Enter a parse tree produced by ExprParser#block.
    def enterBlock(self, ctx:ExprParser.BlockContext):
        pass

    # Exit a parse tree produced by ExprParser#block.
    def exitBlock(self, ctx:ExprParser.BlockContext):
        pass


    # Enter a parse tree produced by ExprParser#if.
    def enterIf(self, ctx:ExprParser.IfContext):
        pass

    # Exit a parse tree produced by ExprParser#if.
    def exitIf(self, ctx:ExprParser.IfContext):
        pass


    # Enter a parse tree produced by ExprParser#while.
    def enterWhile(self, ctx:ExprParser.WhileContext):
        pass

    # Exit a parse tree produced by ExprParser#while.
    def exitWhile(self, ctx:ExprParser.WhileContext):
        pass


    # Enter a parse tree produced by ExprParser#for.
    def enterFor(self, ctx:ExprParser.ForContext):
        pass

    # Exit a parse tree produced by ExprParser#for.
    def exitFor(self, ctx:ExprParser.ForContext):
        pass


    # Enter a parse tree produced by ExprParser#compare.
    def enterCompare(self, ctx:ExprParser.CompareContext):
        pass

    # Exit a parse tree produced by ExprParser#compare.
    def exitCompare(self, ctx:ExprParser.CompareContext):
        pass


    # Enter a parse tree produced by ExprParser#or.
    def enterOr(self, ctx:ExprParser.OrContext):
        pass

    # Exit a parse tree produced by ExprParser#or.
    def exitOr(self, ctx:ExprParser.OrContext):
        pass


    # Enter a parse tree produced by ExprParser#var.
    def enterVar(self, ctx:ExprParser.VarContext):
        pass

    # Exit a parse tree produced by ExprParser#var.
    def exitVar(self, ctx:ExprParser.VarContext):
        pass


    # Enter a parse tree produced by ExprParser#assignment.
    def enterAssignment(self, ctx:ExprParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ExprParser#assignment.
    def exitAssignment(self, ctx:ExprParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ExprParser#equalnotequal.
    def enterEqualnotequal(self, ctx:ExprParser.EqualnotequalContext):
        pass

    # Exit a parse tree produced by ExprParser#equalnotequal.
    def exitEqualnotequal(self, ctx:ExprParser.EqualnotequalContext):
        pass


    # Enter a parse tree produced by ExprParser#addSub.
    def enterAddSub(self, ctx:ExprParser.AddSubContext):
        pass

    # Exit a parse tree produced by ExprParser#addSub.
    def exitAddSub(self, ctx:ExprParser.AddSubContext):
        pass


    # Enter a parse tree produced by ExprParser#parenthesis.
    def enterParenthesis(self, ctx:ExprParser.ParenthesisContext):
        pass

    # Exit a parse tree produced by ExprParser#parenthesis.
    def exitParenthesis(self, ctx:ExprParser.ParenthesisContext):
        pass


    # Enter a parse tree produced by ExprParser#mulDiv.
    def enterMulDiv(self, ctx:ExprParser.MulDivContext):
        pass

    # Exit a parse tree produced by ExprParser#mulDiv.
    def exitMulDiv(self, ctx:ExprParser.MulDivContext):
        pass


    # Enter a parse tree produced by ExprParser#not.
    def enterNot(self, ctx:ExprParser.NotContext):
        pass

    # Exit a parse tree produced by ExprParser#not.
    def exitNot(self, ctx:ExprParser.NotContext):
        pass


    # Enter a parse tree produced by ExprParser#lit.
    def enterLit(self, ctx:ExprParser.LitContext):
        pass

    # Exit a parse tree produced by ExprParser#lit.
    def exitLit(self, ctx:ExprParser.LitContext):
        pass


    # Enter a parse tree produced by ExprParser#and.
    def enterAnd(self, ctx:ExprParser.AndContext):
        pass

    # Exit a parse tree produced by ExprParser#and.
    def exitAnd(self, ctx:ExprParser.AndContext):
        pass


    # Enter a parse tree produced by ExprParser#unaryminus.
    def enterUnaryminus(self, ctx:ExprParser.UnaryminusContext):
        pass

    # Exit a parse tree produced by ExprParser#unaryminus.
    def exitUnaryminus(self, ctx:ExprParser.UnaryminusContext):
        pass


    # Enter a parse tree produced by ExprParser#ternary.
    def enterTernary(self, ctx:ExprParser.TernaryContext):
        pass

    # Exit a parse tree produced by ExprParser#ternary.
    def exitTernary(self, ctx:ExprParser.TernaryContext):
        pass



del ExprParser