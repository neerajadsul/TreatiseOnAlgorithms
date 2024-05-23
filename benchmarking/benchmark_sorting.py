from math import log2
from typing import Callable
import random
from itertools import product

from timing import timeit_wrapper
from sorting import merge_sort, quick_sort, insertion_sort
from datacreator import RwdEffectivePowerWins

def bench_sorting(datapoint_func: Callable, sorting_func: Callable, size_range=(10, 16 + 1)):
    """Benchmark sorting functions using range of input sizes.

    :param datapoint_func: function to generate each data point
    :param sorting_func: sorting function under benchmark
    :param size_range: input size which is power of 2, defaults to (10, 16 + 1) means 1024 to 65535 elements.
    """
    input_size = [2 ** n for n in range(*size_range)]
    print(f'{"Algorithm":>20} | {"O(n)":>5} | {"Size":>12} | {"Time":>6}')
    for m in input_size:
        S = [datapoint_func() for _ in range(m)]
        result, total_time = timeit_wrapper(sorting_func)(S)
        print(f'{sorting_func.__name__:>20} | {int(log2(m)):>5} | {m:>12} | {total_time:>6.3f}')


@timeit_wrapper
def sequential(datapoint_func, sorting_func):
    bench_sorting(datapoint_func, sorting_func, size_range=(14, 20))


if __name__ == "__main__":
    dp_funcs = [random.random, RwdEffectivePowerWins]
    sort_funcs = [merge_sort.merge_sort, merge_sort.merge_sort_iter, quick_sort.quick_sort_lists] #, quick_sort.quick_sort_deque]
    for dp_func, sort_func in product(dp_funcs, sort_funcs):
        sequential(dp_func, sort_func)
        print()
    
    
    
