class VirtualMachine:
    stack = [] # int 
    code = [] # string

    def VirtualMachine(self,code):
        self.code = code.split("\n\r")
        self.code = list(filter(None, self.code))