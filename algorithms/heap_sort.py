from utils.swap import swap


def heapify(array, array_length, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < array_length and array[i] < array[left]:
        largest = left

    if right < array_length and array[largest] < array[right]:
        largest = right

    if largest != i:
        array = swap(array, i, largest)

        heapify(array, array_length, largest)


def heap_sort(array):
    array_length = len(array)

    for i in range(array_length, -1, -1):
        heapify(array, array_length, i)

    for i in range(array_length - 1, 0, -1):
        array = swap(array, i, 0)
        heapify(array, i, 0)

    return array

