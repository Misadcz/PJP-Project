import sys
from antlr4 import *
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
from SymbolTable import SymbolTable
from SymbolTable import Type
from VirtualMachine import VirtualMachine

class VisitorInterp(ExprVisitor):
    
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


    def visitExpression(self, ctx: ExprParser.ExpressionContext):
        if ctx.getChildCount() == 5:
            if self.visit(ctx.getChild(0)):
                return self.visit(ctx.getChild(2))
            else:
                return self.visit(ctx.getChild(4))
        
        if ctx.getChildCount() == 3:
            
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            if ctx.PLUS() != None:
                self.machine.code.append(('add', ''))
                return left + right
            elif ctx.MINUS() != None:
                self.machine.code.append(('sub', ''))
                return left - right
            elif ctx.MULT() != None:
                self.machine.code.append(('mul', ''))
                return left * right
            elif ctx.DIV() != None:
                self.machine.code.append(('div', ''))
                return left / right
            elif ctx.MOD() != None:
                self.machine.code.append(('mod', ''))
                return left % right
            elif ctx.LESSTHAN() != None:
                self.machine.code.append(('lt', ''))
                return left < right
            elif ctx.LESSTHANEQUAL() != None:
                self.machine.code.append(('le', ''))
                return left <= right
            elif ctx.GREATERTHAN() != None:
                self.machine.code.append(('gt', ''))
                return left > right
            elif ctx.GREATERTHANEQUAL() != None:
                self.machine.code.append(('ge', ''))
                return left >= right
            elif ctx.EQUAL() != None:
                self.machine.code.append(('eq', ''))
                return left == right
            elif ctx.getChild(1).getText() == '.':
                res = str(left) + str(right)
                res = res.replace('"', '')
                res = '"' + res + '"'
                return res
            elif ctx.NOTEQUAL() != None:
                self.machine.code.append(('ne', ''))
                return left != right
            elif ctx.AND() != None:
                self.machine.code.append(('and', ''))
                return left and right
            elif ctx.OR() != None:
                self.machine.code.append(('or', ''))
                return left or right
        elif ctx.getChildCount() == 2:
            if ctx.NOT() != None:
                return not self.visit(ctx.getChild(1))
        elif ctx.getChildCount() == 1:
            if ctx.INT() != None:
                self.machine.code.append(('push I', int(ctx.INT().getText())))
                return int(ctx.INT().getText())
            elif ctx.FLOAT() != None:
                self.machine.code.append(('push F', float(ctx.FLOAT().getText())))
                return float(ctx.FLOAT().getText())
            elif ctx.STRING() != None:
                self.machine.code.append(('push S', str(ctx.STRING().getText())))
                return str(ctx.STRING().getText())
            elif ctx.BOOL() != None:
                self.machine.code.append(('push B', True if ctx.BOOL().getText() == 'true' else False))
                return True if ctx.BOOL().getText() == 'true' else False
            elif ctx.variable() != None:
                if ctx.getChild(0).getText() in ('true', 'false'):
                    return True if ctx.getChild(0).getText() == 'true' else False
                self.machine.code.append(('load', ctx.getChild(0).getText()))
                return self.visit(ctx.getChild(0))
        elif ctx.getChildCount() == 3:
            return self.visit(ctx.getChild(1))

    def visitAssignmentType(self, ctx: ExprParser.AssignmentTypeContext):
        type_ = self.visit(ctx.getChild(0))
        for i in range(1, ctx.getChildCount()):
            if ctx.getChild(i).getText() == ',':
                if ctx.getChild(i-2).getText() != '=':
                    if type_ == Type.INT:
                        self.machine.code.append(('push I', 0))
                    elif type_ == Type.FLOAT:
                        self.machine.code.append(('push F', 0.0))
                    elif type_ == Type.STRING:
                        self.machine.code.append(('push S', '""'))
                    elif type_ == Type.BOOL:
                        self.machine.code.append(('push B', False))
                    self.machine.code.append(('save', ctx.getChild(i-1).getText()))
                    self.symbol_table.addSymbolClear(ctx.getChild(i-1).getText(), type_)
                else:
                    if type_ == Type.INT:
                        self.machine.code.append(('push I', self.visit(ctx.getChild(i-1))))
                    elif type_ == Type.FLOAT:
                        self.machine.code.append(('push F', self.visit(ctx.getChild(i-1))))
                    elif type_ == Type.STRING:
                        self.machine.code.append(('push S', self.visit(ctx.getChild(i-1))))
                    elif type_ == Type.BOOL:
                        self.machine.code.append(('push B', self.visit(ctx.getChild(i-1))))
                    self.machine.code.append(('save', ctx.getChild(i-3).getText()))
                    self.symbol_table.addSymbol(ctx.getChild(i-3).getText(), type_, self.visit(ctx.getChild(i-1)))
            elif i == ctx.getChildCount()-1:
                if ctx.getChild(i-1).getText() != '=':
                    if type_ == Type.INT:
                        self.machine.code.append(('push I', 0))
                    elif type_ == Type.FLOAT:
                        self.machine.code.append(('push F', 0.0))
                    elif type_ == Type.STRING:
                        self.machine.code.append(('push S', '""'))
                    elif type_ == Type.BOOL:
                        self.machine.code.append(('push B', False))
                    self.machine.code.append(('save', ctx.getChild(i).getText()))
                    self.symbol_table.addSymbolClear(ctx.getChild(i).getText(), type_)
                else:
                    if type_ == Type.INT:
                        self.machine.code.append(('push I', self.visit(ctx.getChild(i))))
                    elif type_ == Type.FLOAT:
                        self.machine.code.append(('push F', self.visit(ctx.getChild(i))))
                    elif type_ == Type.STRING:
                        self.machine.code.append(('push S', self.visit(ctx.getChild(i))))
                    elif type_ == Type.BOOL:
                        self.machine.code.append(('push B', self.visit(ctx.getChild(i))))
                    self.machine.code.append(('save', ctx.getChild(i-2).getText()))
                    self.symbol_table.addSymbol(ctx.getChild(i-2).getText(), type_, self.visit(ctx.getChild(i)))
        return ''
    
    def visitType(self, ctx: ExprParser.TypeContext):
        if ctx.getChild(0).getText() == 'int':
            return Type.INT
        elif ctx.getChild(0).getText() == 'float':
            return Type.FLOAT
        elif ctx.getChild(0).getText() == 'string':
            return Type.STRING
        elif ctx.getChild(0).getText() == 'bool':
            return Type.BOOL

    def visitStatement(self, ctx: ExprParser.StatementContext):
        if ctx.read() != None:
            return self.visit(ctx.read())
        elif ctx.write() != None:
            return self.visit(ctx.write())
        elif ctx.ifStatement() != None:
            return self.visit(ctx.ifStatement())
        elif ctx.whileStatement() != None:
            return self.visit(ctx.whileStatement())
        elif ctx.assignment() != None:
            return self.visit(ctx.assignment())
        elif ctx.forStatement() != None:
            return self.visit(ctx.forStatement())
        elif ctx.block() != None:
            return self.visit(ctx.block())
        elif ctx.assignmentType() != None:
            return self.visit(ctx.assignmentType())
        
    def visitIfStatement(self, ctx: ExprParser.IfStatementContext):
        if self.visit(ctx.getChild(2)):
            return self.visit(ctx.getChild(4))
        elif ctx.getChildCount() == 7:
            return self.visit(ctx.getChild(6))
        return ''
    
    def visitWhileStatement(self, ctx: ExprParser.WhileStatementContext):
        while self.visit(ctx.getChild(2)):
            self.visit(ctx.getChild(4))
        return ''
    
    def visitForStatement(self, ctx: ExprParser.ForStatementContext):
        self.visit(ctx.getChild(2))
        while self.visit(ctx.getChild(4)):
            self.visit(ctx.getChild(6))
            self.visit(ctx.getChild(8))
        return ''
    
    def visitBlock(self, ctx: ExprParser.BlockContext):
        for i in range(1, ctx.getChildCount()-1):
            self.visit(ctx.getChild(i))
        return ''
   
    def visitRead(self, ctx: ExprParser.ReadContext):
        for i in range(1, ctx.getChildCount()-1):
            if ctx.getChild(i).getText() == ',':
                continue
            input_ = input()
            sym = self.symbol_table.getSymbol(ctx.getChild(i).getText())[1]
            if  sym == Type.INT:
                input_ = int(input_)
            elif sym == Type.FLOAT:
                input_ = float(input_)
            elif sym == Type.BOOL:
                input_ = True if input_ == 'true' else False
            elif sym == Type.STRING:
                input_ = str(input_)
            self.symbol_table.setSymbol(ctx.getChild(i).getText(), input_)
        return ''

    def visitWrite(self, ctx: ExprParser.WriteContext):
        count = 0
        for i in range(1, ctx.getChildCount()-1):
            if ctx.getChild(i).getText() == ',':
                continue
            count = count + 1
            print(self.visit(ctx.getChild(i)), end=' ')
        self.machine.code.append(('print',count ))
        print('')
        return ''

    def visitAssignment(self, ctx: ExprParser.AssignmentContext):
        if ctx.getChild(1).getText() == '=':
            if str(ctx.getChild(2).getText()).__contains__('-'):
                self.machine.code.append(('save', ctx.getChild(0).getText()))
                self.machine.code.append(('load', ctx.getChild(0).getText()))
                self.symbol_table.setSymbol(ctx.getChild(0).getText(), int(ctx.getChild(2).getText()))
            else:
                res = self.visit(ctx.getChild(2))
                if self.symbol_table.getSymbol(ctx.getChild(0).getText())[1] == Type.FLOAT:
                   
                    t = self.symbol_table.getSymbol(ctx.getChild(0).getText())[1]
                    if t == Type.INT:
                        self.machine.code.append(('push I', self.visit(ctx.getChild(2))))
                    elif t == Type.FLOAT:
                        self.machine.code.append(('push F', self.visit(ctx.getChild(2))))
                    elif t == Type.STRING:
                        self.machine.code.append(('push S', self.visit(ctx.getChild(2))))
                    elif t == Type.BOOL:
                        self.machine.code.append(('push B', self.visit(ctx.getChild(2))))
                    self.machine.code.append(('save', ctx.getChild(0).getText()))
                    self.machine.code.append(('load', ctx.getChild(0).getText()))
                    self.machine.code.append('(pop)')
                    self.symbol_table.setSymbol(ctx.getChild(0).getText(), self.toFloat(self.visit(ctx.getChild(2))))
                else:
                    
                    t = self.symbol_table.getSymbol(ctx.getChild(0).getText())[1]
                    if t == Type.INT:
                        self.machine.code.append(('push I', self.visit(ctx.getChild(2))))
                    elif t == Type.FLOAT:
                        self.machine.code.append(('push F', self.visit(ctx.getChild(2))))
                    elif t == Type.STRING:
                        self.machine.code.append(('push S', self.visit(ctx.getChild(2))))
                    elif t == Type.BOOL:
                        self.machine.code.append(('push B', self.visit(ctx.getChild(2))))
                    self.machine.code.append(('save', ctx.getChild(0).getText()))
                    self.machine.code.append(('load', ctx.getChild(0).getText()))
                    self.machine.code.append('(pop)')
                    self.symbol_table.setSymbol(ctx.getChild(0).getText(), self.visit(ctx.getChild(2)))
        return ''
    
    def visitVariable(self, ctx: ExprParser.VariableContext):
        return self.symbol_table.getSymbol(ctx.getChild(0).getText())[2]