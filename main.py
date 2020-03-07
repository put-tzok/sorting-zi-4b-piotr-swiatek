import math

def fill_increasing(size):
    array = []
    for i in range(size):
        array.append(i)
    return array


def fill_decreasing(size):
    array = []
    actual_size = size if size >= 0 else size * -1
    for i in range(actual_size):
        array.append(i * -1)
    return array


def fill_vshape(size):
    array = []
    second_starting_point = 1 if size % 2 == 0 else 0
    for i in range(size, 1, -2):
        array.append(i)
    for i in range(second_starting_point, size, 2):
        array.append(i)
    return array


print(fill_vshape(100))




