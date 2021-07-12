from collections import Counter
from Calc.Addition import addition

def mode(data):
    data.sort()

    list1 = []

    i = 0
    while i < len(data) :
        list1.append(data.count(data[i]))
        addition(i,1)

    d1 = dict(zip(data, list1))
    d2={k for (k,v) in d1.items() if v == max(list1)}

    return d2