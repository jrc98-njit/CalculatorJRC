import math
from Stats.Variance import variance
from Calc.SquareRoot import squareroot

def standardDeviation(data):
    return squareroot(variance(data))
