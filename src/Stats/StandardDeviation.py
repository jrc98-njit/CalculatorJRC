import math
from Stats.Variance import variance
from Calc.SquareRoot import squareroot

def standardDeviation(data):
    numValues = len(data)
    if (numValues == 0):
        raise Exception('empty list passed to list')
    return squareroot(variance(data))
