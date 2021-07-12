def division (a, b):
    if (b == 0):
        raise Exception('cannot divide by zero')

    a = int (a)
    b = int (b)
    c = float(a / b)
    return c
