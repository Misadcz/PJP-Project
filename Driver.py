import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from VisitorInterp import VisitorInterp
from VirtualMachine import VirtualMachine

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
        code = visitor.visit(tree)
     #   print(tree.toStringTree(recog=parser))
        
        fileta = open("output.txt", "w")
       
        happened = 0
        for i in range(len(code)):
            if happened == 1:
                happened = 0
                continue
            if code[i] == 'uminus':
                code[i] = code[i+1]
                code[i+1] = 'uminus'
                happened = 1

        for i in range(len(code)):
            if code[i] == 'pop' and 'load' in code[i-1] and 'save' in code[i-2] and 'save' in code[i+1] and 'load' in code[i+2]:
                #remove this code[i]
                for j in range(i, len(code)-1):
                    code[j] = code[j+1]
                # smaller size of code
                code.pop()
                break
                
                


        for line in code:
            fileta.write(str(line) + '\n')

        virtual = VirtualMachine()
        virtual.run(code)


if __name__ == '__main__':
    main(sys.argv)