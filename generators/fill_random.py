import random


def fill_random(size):
    array = []
    for i in range(size):
        array.append(random.randint(0, size))
    return array
