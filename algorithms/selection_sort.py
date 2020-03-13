from utils.swap import swap


def selection_sort(array):
    array_length = len(array)

    for i in range(array_length):
        min_index = i
        for j in range(i + 1, array_length):
            if array[j] < array[min_index]:
                min_index = j
        array = swap(array, i, min_index)

