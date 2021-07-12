from Calc.Addition import addition
from Calc.Subtraction import subtraction
from Calc.Multiplication import multiplication
from Calc.Division import division
from Calc.Square import square
from Calc.SquareRoot import squareroot

class Calculator:

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract (self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def division(self, a, b):
        self.result = division(a, b)
        return self.result


    def square(self, a):
        self.result = square(a)
        return self.result

    def squareroot(self, a):
        self.result = squareroot(a)
        return self.result
