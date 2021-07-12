import math
from Stats.Mean import mean
from Calc.Division import division


def median(data):
    numValues = len(data)
    data.sort()

    if (numValues % 2 == 0):
        median1 = data[numValues//2]
        median2 = data[numValues//2 - 1]
        median = mean(data)
    else:
        median = data[numValues//2]
    return median

