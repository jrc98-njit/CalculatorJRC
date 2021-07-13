import math
from Stats.Mean import mean
from Calc.Addition import addition
from Calc.Division import division
from Calc.Subtraction import subtraction
from Calc.Square import square


def variance(data):
    numValues = len(data)
    if (numValues == 0):
        raise Exception('empty list passed to list')

    meanValue = mean(data)

    total = 0
    for i in data:
        total = addition(total, square(subtraction(i,meanValue)))

    val = division(total,len(data)-1)
    return val

