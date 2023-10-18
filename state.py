import reflex as rx
from calculator import style

#-----to do-----:
#add more state so that u can use keybord for input aswell
#add more conditiions to concat about the bracket and decimal
#add more conditions in deletion about the bracket and decimal
#create similar for decimal as well


class State(rx.State):
    ans : str = "Ans"
    input_text : str =""
    bracket_open : bool = True
    operations_stack : list = []
    operands_stack : list = []
    nums : list = ["0","1","2","3","4","5","6","7","8","9","."]
    expression : str = ""
    brackets: list = ["(",")"]
    operations : list = ["+","-","*","/"]


    def concat(self,value):
        self.expression+=value

    def delete(self):
        self.input_text=self.input_text[:-1]

    def bracket(self):
        if self.bracket_open:
            self.concat("(")
        else :
            self.concat(")")
        self.bracket_open = not (self.bracket_open)

    def AC(self):
        self.expression = ""
        self.ans = ""

    def solve(self):
        while len(self.expression)!=0 :
            if self.expression[0] in self.operations :
                self.operations_stack.append(self.expression[0])
                self.expression=self.expression[1:]

            else :
                temp = ""
                while len(self.expression)>0 and self.expression[0] in self.nums :
                    temp+=self.expression[0]
                    self.expression=self.expression[1:]
                self.operands_stack.append(temp)

                if len(self.operations_stack)>0 and self.operations_stack[-1] in self.operations :
                    num1 = float(self.operands_stack[-2])
                    num2 = float(self.operands_stack[-1])
                    self.operands_stack=self.operands_stack[:-2]

                    if self.operations_stack[-1] == "*":
                        self.operands_stack.append(str(num1*num2))

                    elif self.operations_stack[-1] == "/":
                        self.operands_stack.append(str(num1/num2))

                    elif self.operations_stack[-1] == "+" :
                        self.operands_stack.append(str(num1+num2))

                    elif self.operations_stack[-1] == "-":
                        self.operands_stack.append(str(num1-num2))

                    self.operations_stack=self.operations_stack[:-1]

        self.ans=self.operands_stack[0]