import sys
from antlr4 import *
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
from SymbolTable import SymbolTable
from SymbolTable import Type
from VirtualMachine import VirtualMachine

class VisitorInterp(ExprVisitor):
    label_count = 0
    jmp_count = 0
    was = 0
    
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.machine = VirtualMachine()
        

    def toFloat(self, value):
        if type(value) == int:
            return float(value)
        return value
    
    def visitProg(self, ctx:ExprParser.ProgContext):
            for i in range(ctx.getChildCount()):
                self.visit(ctx.getChild(i))
            self.checkAll()
            return self.machine.code
    
    def checkAll(self):
        print('\n')
        for key in self.symbol_table.memory:
            print(key, self.symbol_table.memory[key])
        print("------")

    def visitAnd(self, ctx: ExprParser.AndContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        self.machine.code.append('and')
        return left and right

    def visitOr(self, ctx: ExprParser.OrContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        self.machine.code.append('or')
        return left or right
    
    def visitNot(self, ctx: ExprParser.NotContext):
        var = not self.visit(ctx.expression())
        self.machine.code.append('not')
        return var

    def visitAddSub(self, ctx: ExprParser.AddSubContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if type(left) == float or type(right) == float:
            if type(left) == int or  type(right) == int:
                self.machine.code.append('itof')
        if ctx.op.type == ExprParser.PLUS:
            self.machine.code.append('add')
            if type(left) == str or type(right) == str:
                print("Error: Cannot add string with number")
                return ''
            if type(left) == float or type(right) == float:
                return self.toFloat(left) + self.toFloat(right)
            return left + right
        if type(left) == str and type(right) == str:
            self.machine.code.append('concat')
            return str(left) + str(right)
        if type(left) == str or type(right) == str:
            print("Error: Cannot add string with number")
            return ''
        self.machine.code.append('sub')
        if type(left) == float or type(right) == float:
            return self.toFloat(left) - self.toFloat(right)
        return left - right
        
    def visitMulDiv(self, ctx: ExprParser.MulDivContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if type(left) == float or type(right) == float:
            if type(left) == int or  type(right) == int:
                self.machine.code.append('itof')
        if ctx.op.type == ExprParser.MULT:
            self.machine.code.append('mul')
            if type(left) == float or type(right) == float:
                return self.toFloat(left) * self.toFloat(right)
            return left * right
        if ctx.op.type == ExprParser.DIV:
            self.machine.code.append('div')
            if type(left) == float or type(right) == float:
                return self.toFloat(left) / self.toFloat(right)
            return left / right
        if type(left) == float or type(right) == float:
            print("Error: Cannot mod int by float")
            return ''
        self.machine.code.append('mod')
        return left % right
    
    def visitInt(self, ctx: ExprParser.IntContext):
        self.machine.code.append('push '+'I '+str(ctx.INT().getText()))
        return int(ctx.INT().getText())
    
    def visitFloat(self, ctx: ExprParser.FloatContext):
        self.machine.code.append('push '+'F '+str(ctx.FLOAT().getText()))
        return float(ctx.FLOAT().getText())
    
    def visitId(self, ctx: ExprParser.IdContext):
        self.machine.code.append('load '+ctx.ID().getText())
        return self.symbol_table.getSymbol(ctx.ID().getText())[0]

    def visitAssignment(self, ctx: ExprParser.AssignmentContext):
        value = self.visit(ctx.expression())    
        #cant float to int
        if self.symbol_table.getSymbol(ctx.variable().getText())[1] == Type.INT and type(value) == float:
            print("Error: Cannot assign float to int")
            return None
        if self.symbol_table.getSymbol(ctx.variable().getText())[1] == Type.FLOAT and type(value) == int:
            self.machine.code.append('itof')
            self.symbol_table.setSymbol(ctx.variable().getText(), self.toFloat(value))
        else:
            self.symbol_table.setSymbol(ctx.variable().getText(), value)
        self.machine.code.append('save '+ctx.variable().getText())
        self.machine.code.append('load '+ctx.variable().getText())
        #what if i=j=k=55, there will be pop just with i
        
        if ctx.expression().getText().count('=') > 1:
            self.machine.code.append('pop')
        
        if ctx.expression().getText().count('=') == 0:
            self.machine.code.append('pop')
            
        return value

    def visitWrite(self, ctx: ExprParser.WriteContext):
        count = 0
        for i in range(1, ctx.getChildCount()-1):
            if ctx.getChild(i).getText() == ',':
                continue
            count = count + 1
            print(self.visit(ctx.getChild(i)), end=' ')
        self.machine.code.append('print '+str(count))
        print()
        return None
    
    def visitVar(self, ctx: ExprParser.VarContext):
        if ctx.getChild(0).getText() == 'true':
            self.machine.code.append('push B '+'true')
            return True
        if ctx.getChild(0).getText() == 'false':

            self.machine.code.append('push B '+'false')
            return False
        self.machine.code.append('load '+ctx.variable().getText())
        return self.symbol_table.getSymbol(ctx.variable().getText())[2]
        
        
    
    def visitString(self, ctx: ExprParser.StringContext):
        self.machine.code.append('push '+'S '+str(ctx.STRING().getText()))
        if str(ctx.STRING().getText())[1:-1] != "":
            return str(ctx.STRING().getText())[1:-1]
        return " "
    
    def visitBool(self, ctx: ExprParser.BoolContext):
        self.machine.code.append('push '+'B '+ctx.BOOL().getText() == "true")
        return ctx.BOOL().getText() == "true"

    def visitIf(self, ctx: ExprParser.IfContext):
        self.visit(ctx.expression())

        self.machine.code.append('fjmp ' + str(self.label_count))

        self.visit(ctx.statement(0))

        self.machine.code.append('jmp ' + str(self.label_count+1))
        self.machine.code.append('label ' + str(self.label_count))
        self.label_count += 1

    
        if ctx.statement(1) != None:
            self.visit(ctx.statement(1))
            self.machine.code.append('label ' + str(self.label_count))
            self.label_count += 1
        else:
            self.machine.code.append('label ' + str(self.label_count))
            self.label_count += 1
            
    
    def visitBlock(self, ctx: ExprParser.BlockContext):
        for i in range(1, ctx.getChildCount()-1):
            self.visit(ctx.getChild(i))
        return None

    def visitWhile(self, ctx: ExprParser.WhileContext):
        self.machine.code.append('label ' + str(self.label_count))
        self.visit(ctx.expression())
        self.machine.code.append('fjmp ' + str(self.label_count+1))
        self.visit(ctx.statement())
        self.machine.code.append('jmp ' + str(self.label_count))
        self.machine.code.append('label ' + str(self.label_count+1))
        self.label_count += 2
        return None

    def visitFor(self, ctx: ExprParser.ForContext):
        self.visit(ctx.expression())
        while self.visit(ctx.expression()):
            self.visit(ctx.statement())
            self.visit(ctx.expression())
        return None

    def visitDeclaration(self, ctx: ExprParser.DeclarationContext):
        type_ = ctx.getChild(0).getText()
        for i in range(1, ctx.getChildCount()-1):
            if ctx.getChild(i).getText() == ',':
                continue
            if type_ == 'int':
                self.machine.code.append('push '+'I '+'0')
            elif type_ == 'float':
                self.machine.code.append('push '+'F '+'0.0')
            elif type_ == 'bool':
                self.machine.code.append('push '+'B '+'true')
            elif type_ == 'string':
                self.machine.code.append('push '+'S '+'""')

            self.machine.code.append('save '+ctx.getChild(i).getText())
            self.symbol_table.addSymbolClear(ctx.getChild(i).getText(), type_)

    def visitLiteral(self, ctx: ExprParser.LiteralContext):
        return self.visit(ctx.getChild(0))

    def visitRead(self, ctx: ExprParser.ReadContext):
        for i in range(1, ctx.getChildCount()-1):
            if ctx.getChild(i).getText() == ',':
                continue
            value = input()
            type_ = self.symbol_table.getSymbol(ctx.getChild(i).getText())[1]
            if type_ == Type.INT:
                self.machine.code.append('read I')
                value = int(value)
            elif type_ == Type.FLOAT:
                self.machine.code.append('read F')
                value = float(value)
            elif type_ == Type.BOOL:
                self.machine.code.append('read B')
                value = value == "true"
            else:
                self.machine.code.append('read S')
            self.machine.code.append('save '+ctx.getChild(i).getText())
            self.symbol_table.setSymbol(ctx.getChild(i).getText(),value)
        return None

    def visitCompare(self, ctx: ExprParser.CompareContext):
        left = self.visit(ctx.expression(0))
        if type(left) == int and ctx.expression(1).getText().__contains__('.'):
                self.machine.code.append('itof')
        right = self.visit(ctx.expression(1))
        
        if ctx.op.type == ExprParser.LESSTHAN:
            self.machine.code.append('lt')
            return self.toFloat(left) < self.toFloat(right)
        self.machine.code.append('gt')
        return self.toFloat(left) > self.toFloat(right)
    
    def visitUnaryminus(self, ctx: ExprParser.UnaryminusContext):
        self.machine.code.append('uminus')
        return -self.visit(ctx.expression())
    
    def visitParenthesis(self, ctx: ExprParser.ParenthesisContext):
        return self.visit(ctx.expression())
    
    def visitEmpty(self, ctx: ExprParser.EmptyContext):
        return None
    
    def visitTernary(self, ctx: ExprParser.TernaryContext):
        if self.visit(ctx.expression(0)):
            return self.visit(ctx.expression(1))
        return self.visit(ctx.expression(2))
    
    def visitEqualnotequal(self, ctx: ExprParser.EqualnotequalContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.type == ExprParser.EQUAL:
            self.machine.code.append('eq')
            return left == right
        self.machine.code.append('eq')
        self.machine.code.append('not')
        return left != right

