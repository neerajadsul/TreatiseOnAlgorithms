from math import log2
from typing import Callable
import random
from itertools import product
from multiprocessing import Pool

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
    for m in input_size:
        S = [datapoint_func() for _ in range(m)]
        result, total_time = timeit_wrapper(sorting_func)(S)
        print(f'{sorting_func.__name__:>20} | {int(log2(m)):>5} | {m:>12} | {total_time:>6.3f}')


@timeit_wrapper
def sequential(dp_funcs, sort_funcs):
    print(f'{"Algorithm":>20} | {"O(n)":>5} | {"Size":>12} | {"Time":>6}')
    for dp_func, sort_func in product(dp_funcs, sort_funcs):
        bench_sorting(dp_func, sort_func, size_range=(14, 19))
        print()


@timeit_wrapper
def multiproc_pools(dp_funcs, sort_funcs):
    print(f'{"Algorithm":>20} | {"O(n)":>5} | {"Size":>12} | {"Time":>6}')
    dpf_spf = tuple(product(dp_funcs, sort_funcs, [(14,19)]))
    with Pool(16) as p:
        p.starmap(bench_sorting, dpf_spf)
    p.join()


if __name__ == "__main__":
    dp_funcs = [random.random, RwdEffectivePowerWins]
    sort_funcs = [merge_sort.merge_sort, merge_sort.merge_sort_iter, quick_sort.quick_sort_lists, quick_sort.quick_sort_deque, sorted]
    
    results, total_time = sequential(dp_funcs=dp_funcs, sort_funcs=sort_funcs)
    print(f'Sequential Total Time: {total_time}s')
    
    results, total_time = multiproc_pools(dp_funcs=dp_funcs, sort_funcs=sort_funcs)
    print(f'Multiprocessing Total Time: {total_time}s')
