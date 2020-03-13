# Quick sort with pivot as last element of an array


def partition(array, low, high):
    i = (low - 1)
    pivot = array[high]

    for j in range(low, high):
        if array[j] < pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(array, start, stop):
    if start < stop:
        pivot = partition(array, start, stop)

        quick_sort(array, start, pivot - 1)
        quick_sort(array, pivot + 1, stop)


