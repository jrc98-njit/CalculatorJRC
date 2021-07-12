import random


def getSample(data, sample_size):
    random_values = random.choices(data, sample_size)

    return random_values