import sys
from antlr4 import *
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
from SymbolTable import SymbolTable
from SymbolTable import Type

class VisitorInterp(ExprVisitor):
    
    def __init__(self):
        self.symbol_table = SymbolTable()
    
    def toFloat(self, value):
        if isinstance(value, int):
            return float(value)
        else:
            return value
    
    def visitProg(self, ctx:ExprParser.ProgContext):
            for i in range(ctx.getChildCount()):
                self.visit(ctx.getChild(i))
        #    self.checkAll()
            return ''
    
    def visitAssignStatement(self, ctx: ExprParser.AssignStatementContext):
        type = ctx.children[0].getText()
        for i in range(1,ctx.getChildCount()):
            if i == ctx.getChildCount()-1:
                if ctx.children[i].getText().isdigit():
                    if type == 'int':
                        self.symbol_table.addSymbol(ctx.children[i-2].getText(), type, int(ctx.children[i].getText()))
                    if type == 'float':
                        self.symbol_table.addSymbol(ctx.children[i-2].getText(), type, float(ctx.children[i].getText()))
                else:
                    self.symbol_table.addSymbolClear(ctx.children[i].getText(), type)
            elif ctx.children[i].getText() == ',':
                if ctx.children[i-1].getText().isdigit():
                    if type == 'int':
                        self.symbol_table.addSymbol(ctx.children[i-3].getText(), type, int(ctx.children[i-1].getText()))
                    if type == 'float':
                        self.symbol_table.addSymbol(ctx.children[i-3].getText(), type, float(ctx.children[i-1].getText()))
                else:
                    self.symbol_table.addSymbolClear(ctx.children[i-1].getText(), type)



    def visitOperationStatement(self, ctx: ExprParser.OperationStatementContext):
        
        if ctx.children[1].getText() == '+':
            if str(ctx.children[2].getText()).__contains__('.'):
                self.symbol_table.setSymbol(ctx.children[0].getText(), self.symbol_table.getSymbol(ctx.children[0].getText())[2]+ float(ctx.children[2].getText()))
            elif str(ctx.children[2].getText()).isdigit():
                self.symbol_table.setSymbol(ctx.children[0].getText(), self.symbol_table.getSymbol(ctx.children[0].getText())[2]+ int(ctx.children[2].getText()))
            elif self.symbol_table.getSymbol(ctx.children[2].getText())[1] == Type.INT:
                self.symbol_table.setSymbol(ctx.children[0].getText(), int(self.symbol_table.getSymbol(ctx.children[0].getText())[2])+ int(self.symbol_table.getSymbol(ctx.children[2].getText())[2]))
            else:
                self.symbol_table.setSymbol(ctx.children[0].getText(), float(self.symbol_table.getSymbol(ctx.children[0].getText())[2])+ float(self.symbol_table.getSymbol(ctx.children[2].getText())[2]))
            return ''
    
        if ctx.getChildCount() > 3:
            if ctx.children[1].getText() == '=' and ctx.children[3].getText() == '=':
                self.symbol_table.setSymbol(ctx.children[0].getText(), ctx.children[4].getText())
                self.symbol_table.setSymbol(ctx.children[2].getText(), ctx.children[4].getText())
                return ''
        
        lst = []
        for i in range(2,ctx.getChildCount()):
            if ctx.children[i].getText() not in ('*', '/', '+', '-', '(', ')') and ctx.children[i].getText().isdigit() != True:
                if self.symbol_table.getSymbol(ctx.children[i].getText())[1] == Type.INT:
                    lst.append(int(self.symbol_table.getSymbol(ctx.children[i].getText())[2]))
                else:
                    lst.append(float(self.symbol_table.getSymbol(ctx.children[i].getText())[2]))
            else:
                if ctx.children[i].getText().isdigit():
                    lst.append(int(ctx.children[i].getText()))
                else:
                    lst.append(ctx.children[i].getText())
        
        for i in range(len(lst)):
            if lst[i] == '*':
                lst[i] = lst[i-1] * lst[i+1]
                lst.pop(i-1)
                lst.pop(i)
                break
            if lst[i] == '/':
                lst[i] =lst[i-1] / lst[i+1]
                lst.pop(i-1)
                lst.pop(i)
                break
        
        still = True
        while still == True:
            still = False
            for i in range(len(lst)):
                if lst[i] == '+':
                    lst[i] = lst[i-1] + lst[i+1]
                    lst.pop(i-1)
                    lst.pop(i)
                    still = True
                    break
                if lst[i] == '-':
                    lst[i] = lst[i-1] - lst[i+1]
                    lst.pop(i-1)
                    lst.pop(i)
                    still = True
                    break   
        

        if str(lst[0]).__contains__('.'):
            if self.symbol_table.getSymbol(ctx.children[0].getText())[1] == Type.INT:
                line = str(ctx.children[0].symbol.line) + ':' + str(ctx.children[0].symbol.column)
                print (line+' - Variable \'' + ctx.children[0].getText() + '\' is int, but assigned value is float')
                

            else:
                self.symbol_table.setSymbol(ctx.children[0].getText(), lst[0])
        else:
                self.symbol_table.setSymbol(ctx.children[0].getText(), lst[0])
            

    def checkAll(self):
        for key in self.symbol_table.memory:
            print(key, self.symbol_table.memory[key])
        print("------")
        pass

    def visitReadStatement(self, ctx: ExprParser.ReadStatementContext):
        text = input()
        self.symbol_table.setSymbol(ctx.children[1].getText(), int(text))
    
    def visitWriteStatement(self, ctx: ExprParser.WriteStatementContext):
        if ctx.children[1].getText()[0] == '"' and ctx.children[1].getText()[-1] == '"':
                print(ctx.children[1].getText(), end=' ')
        for i in range(2, ctx.getChildCount()):
            print(ctx.children[i].getText(), end=' ')
            if ctx.children[i].getText().__contains__('"'):
                self.visit(ctx.children[i])
            elif ctx.children[i].getText() == ',':
                continue
            else:
                if (ctx.children[i].getText()).__contains__('<') or (ctx.children[i].getText()).__contains__('>') or (ctx.children[i].getText()).__contains__('<=') or (ctx.children[i].getText()).__contains__('>=') or (ctx.children[i].getText()).__contains__('==') or (ctx.children[i].getText()).__contains__('!='):
                    print(self.visit(ctx.children[i]), end=' ')
                else:
                    var = self.symbol_table.getSymbol(ctx.children[i].getText())
                    print(var[2], end=' ')
                
        print('')        
    
    def visitForStatement(self, ctx: ExprParser.ForStatementContext):
        while self.visit(ctx.children[4]):
            for i in range(4, ctx.getChildCount()):
                self.visit(ctx.children[i])
        
    def visitWhileStatement(self, ctx: ExprParser.WhileStatementContext):
        while self.visit(ctx.children[2]):
            for i in range(0, ctx.getChildCount()):
                self.visit(ctx.children[i])

    def visitIfStatement(self, ctx: ExprParser.IfStatementContext):   
        savepoint = -1
        for i in range(0, ctx.getChildCount()):
            if ctx.children[i].getText() == 'else':
                savepoint = i
                break
        if savepoint != -1:
            if self.visit(ctx.children[2]):
                for i in range(4, savepoint):
                    self.visit(ctx.children[i])
        else:
            if self.visit(ctx.children[2]):
                for i in range(4, ctx.getChildCount()):
                    self.visit(ctx.children[i])
       
            
            
    
    def visitCond(self, ctx: ExprParser.CondContext):

        if ctx.children[0].getText() == 'true':
            return True
        if ctx.children[0].getText() == 'false':
            return False
        
        
        
     #   if ctx.children[0].getText().__contains__('"'):
    #       left = ctx.children[0].getText()
     #       right = ctx.children[2].getText()
     #   else:
        if ctx.children[0].getText().isdigit():
            left = float(ctx.children[0].getText())
        else:
            left = float(self.symbol_table.getSymbol(ctx.children[0].getText())[2])
        if ctx.children[2].getText().isdigit():
            right = float(ctx.children[2].getText())
        else:
            right = float(self.symbol_table.getSymbol(ctx.children[2].getText())[2])

        middle = ctx.children[1].getText()
        
        if middle == '<':
            return left < right
        if middle == '>':
            return left > right
        if middle == '<=':
            return left <= right
        if middle == '>=':
            return left >= right
        if middle == '==':
            return left == right
        if middle == '!=':
            return left != right
        if middle == '&&':
            return left and right
        if middle == '||':
            return left or right
        if middle == '!':
            return not left
        
