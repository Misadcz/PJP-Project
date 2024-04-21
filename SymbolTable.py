
import sys
from antlr4 import *
from enum import Enum

class Type(Enum):
    INT = 0
    FLOAT = 1
    ERROR = 2
    STRING = 3
    BOOL = 4



class SymbolTable:
    
    memory = {}
    
    def addSymbolClear(self, name, type):
        if name in self.memory:
            print("Error: variable "+name+" already declared")
        else:
            if type == 'int':
                self.memory[name] = (name,Type.INT,0)
            if type == 'float':
                self.memory[name] = (name,Type.FLOAT,0.0)
            if type == 'string':
                self.memory[name] = (name,Type.STRING,"")
            if type == 'bool':
                self.memory[name] = (name,Type.BOOL,True)
                
    def addSymbol(self, name, type,value):
        if name in self.memory:
            print("Error: variable "+name+" already declared")
        else:
            if type == 'int':
                self.memory[name] = (name,Type.INT,int(value))
            if type == 'float':
                self.memory[name] = (name,Type.FLOAT,float(value))
            if type == 'string':
                if value[0] == '"':
                    value = str(value)[1:]
                    value = str(value)[:len(value)-1]
                self.memory[name] = (name,Type.STRING,str(value))
            if type == 'bool':
                self.memory[name] = (name,Type.BOOL,bool(value))
            
    
    def getSymbol(self, name):
        if name in self.memory:
            return self.memory[name]
        else:
            print("Error: variable "+name+" not declared")
            return (Type.ERROR, 0)
    
    def setSymbol(self, name, value):
        if name in self.memory:
            if self.memory[name][1] == Type.STRING:
                if value[0] == '"':
                    value = str(value)[1:]
                    value = str(value)[:len(value)-1]
            self.memory[name] = (name, self.memory[name][1], value)

        else:
            print("Error: variable "+name+" not declared")