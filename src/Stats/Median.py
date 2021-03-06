import math
from Stats.Mean import mean
from Calc.Division import division


def median(data):
    numValues = len(data)
    if (numValues == 0):
        raise Exception('empty list passed to list')
    data.sort()

    if (numValues % 2 == 0):
        median_data = []
        median_data.append(data[numValues//2])
        median_data.append(data[numValues//2 - 1])
        median = mean(median_data)
    else:
        median = data[numValues//2]
    return median

