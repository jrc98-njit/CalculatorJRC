import random
from random import uniform

# randrange gives you an integral value
def getRandomInt(low, high):
    return random.randint(low, high)

def getRandomFloat(low, high):
    return uniform(low, high)

def getRandomIntSeed(low, high, seed):
    random.seed(seed)
    return getRandomInt(low, high)

def getRandomNumbersInt(low, high, seed, total):
    data = []
    for i in range(total):
        # Random number with seed
        random.seed(seed)
        data.append(random.randint(low, high))
    return data

def getRandomNumbersFloat(low, high, seed, total):
    data = []
    for i in range(total):
        # Random number with seed
        random.seed(seed)
        data.append(getRandomFloat(low, high))
    return data

