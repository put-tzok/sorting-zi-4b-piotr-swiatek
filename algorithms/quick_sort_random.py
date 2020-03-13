# Quick sort with pivot as random element inside of an array
import random
from utils.swap import swap


def partition_rand(arr, start, stop):
    rand_pivot = random.randrange(start, stop)

    arr = swap(arr, start, rand_pivot)
    return partition(arr, start, stop)


def partition(arr, start, stop):
    pivot = start
    i = start - 1
    j = stop + 1
    while True:
        while True:
            i = i + 1
            if arr[i] >= arr[pivot]:
                break
        while True:
            j = j - 1
            if arr[j] <= arr[pivot]:
                break
        if i >= j:
            return j
        arr = swap(arr, i, j)


def quick_sort_random(arr, start, stop):
    if start < stop:
        pivot_index = partition_rand(arr, start, stop)

        quick_sort_random(arr, start, pivot_index)
        quick_sort_random(arr, pivot_index + 1, stop)

    return arr

