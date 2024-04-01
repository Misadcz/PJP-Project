import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from VisitorInterp import VisitorInterp

def main(argv):
    input_stream = FileStream(sys.argv[1])
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)
    tree = parser.prog()
    
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Number of syntax errors: ", parser.getNumberOfSyntaxErrors())
    else:
        visitor = VisitorInterp()
        print(visitor.visit(tree))
    

if __name__ == '__main__':
    main(sys.argv)