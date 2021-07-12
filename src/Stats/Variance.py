import math
from Stats.Mean import mean
from Calc.Addition import addition
from Calc.Division import division
from Calc.Square import square


def variance(data):
    meanValue = mean(data)
    total = 0
    for i in data:
        total = addition(total, square(i-meanValue))
    return division(total,len(data)-1)


