from utils.measure_time import measure_time


def insertion_sort(array):
    array_length = len(array)

    for i in range(1, array_length):
        key = array[i]

        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key


def test_insertion_sort(array):
    # in order to not mutate array directly here copy of array is being made
    array_copy = array
    measure_time(insertion_sort, array_copy)

