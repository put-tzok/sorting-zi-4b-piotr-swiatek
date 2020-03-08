def fill_v_shape(size):
    array = []
    second_starting_point = 1 if size % 2 == 0 else 0
    for i in range(size, 1, -2):
        array.append(i)
    for i in range(second_starting_point, size, 2):
        array.append(i)
    return array
