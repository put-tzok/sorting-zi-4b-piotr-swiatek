def selection_sort(array):
    array_length = len(array)

    for i in range(array_length):
        min_index = i
        for j in range(i + 1, array_length):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array
