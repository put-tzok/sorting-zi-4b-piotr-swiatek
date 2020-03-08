def fill_decreasing(size):
    array = []
    actual_size = size if size >= 0 else size * -1
    for i in range(actual_size):
        array.append(i * -1)
    return array
