
def addition(a, b):
    a = int(a)
    b = int(b)
    c = a+b
    return c


def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = a - b
    return c


def multiplication(a, b):
    a = int (a)
    b = int (b)
    c = a * b
    return c


def divison (a, b):
    a = int (a)
    b = int (b)
    c = a / b
    return c

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
        self.result = divison(a, b)
        return self.result




