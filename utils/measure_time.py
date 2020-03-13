import time
ONE_SECOND = 1000


def measure_time(algorithm, test_set, is_quick_sort):
    start_time = time.time()
    if is_quick_sort:
        algorithm(test_set, 0, len(test_set) - 1)
    else:
        algorithm(test_set)
    end_time = time.time()
    return round((end_time - start_time) * ONE_SECOND, 3)

