from Calc.Addition import addition
from Calc.Division import division


def mean(data):
    numValues = len(data)
    if (numValues == 0):
        raise Exception('empty list passed to list')

    total = 0
    for num in data:
        if (isinstance(num,str)):
            raise Exception('List must contain numbers')
        total = addition(total, num)
    return division(total, numValues)
