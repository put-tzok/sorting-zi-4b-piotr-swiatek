from utils.measure_time import measure_time

from generators.fill_increasing import fill_increasing
from generators.fill_decreasing import fill_decreasing
from generators.fill_v_shape import fill_v_shape
from generators.fill_random import fill_random

from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.heap_sort import heap_sort
from algorithms.quick_sort import quick_sort
from algorithms.quick_sort_random import quick_sort_random

ONE_SECOND = 1000


def is_quick_sort(algorithm):
    return algorithm == quick_sort or algorithm == quick_sort_random


def create_test_set(n):
    return {
        'increasing': fill_increasing(n),
        'decreasing': fill_decreasing(n),
        'v_shape': fill_v_shape(n),
        'random': fill_random(n)
    }


def test_execution_time(algorithm, test_set, test_set_name):
    # in order to not mutate array directly here copy of array is being made
    test_set_copy = test_set
    run_time = measure_time(algorithm, test_set_copy, is_quick_sort(algorithm))
    print('{} at {} test set took {} ms'.format(algorithm, test_set_name, run_time))


def start_tests(n):
    algorithms = [selection_sort, insertion_sort, heap_sort, quick_sort, quick_sort_random]
    test_sets = create_test_set(n)

    for algorithm in algorithms:
        for test_set in test_sets:
            try:
                test_execution_time(algorithm, test_sets[test_set], test_set)
            except RuntimeError as re:
                print('Error in {}'.format(re))


