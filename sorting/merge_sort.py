"""Merge sort is divide-and-conquer sorting technique.
Implemented as in-place sort.
Split the sequence in two halves S1 and S2, 
Sort each half S1 and S2 recusively.
Merge two halves S1 and S2 into S
"""
from operator import lt, gt
from math import ceil, log2


def _merge(S1, S2, S, desc):
    """Merge two sequences S1 and S2 into S in ascending order.
    
    Args:
        S1, S2: two halves of sequence S
        S: sequence to merge into
        desc: sorting order, default ascending
    """
    i, j = 0, 0
    comparison = gt if desc else lt
    while (i+j) < len(S):
        if j==len(S2) or (i < len(S1) and comparison(S1[i], S2[j])):
            S[i + j] = S1[i]
            i += 1
        else:
            S[i + j] = S2[j]
            j += 1


def merge_sort(S, desc=False):
    """Sorts given sequence in ascending order using Merge Sorting algorithm.
    
    Args:
        S: sequence
        desc: sorting order, default False that si ascending
    """
    
    n = len(S)
    if n < 2:
        return
    # Split in two halve
    mid = n // 2
    S1 = S[:mid]
    S2 = S[mid:]
    
    # Conquer
    merge_sort(S1, desc=desc)
    merge_sort(S2, desc=desc)
    
    # Merge
    _merge(S1, S2, S, desc=desc)


def _merge_iter(src, dest, start, inc):
    x = start
    y = start + inc
    z = start
    
    end_1 = start + inc
    end_2 = min(start + 2*inc, len(src))
    
    while x < end_1 and y < end_2:
        if src[x] < src[y]:
            dest[z] = src[x]
            x += 1
        else:
            dest[z] = src[y]
            y += 1
        z += 1
    if x < end_1:
        dest[z:end_2] = src[x:end_1]
    elif y < end_2:
        dest[z:end_2] = src[y:end_2]

    
def merge_sort_iter(S, desc=False):
    n = len(S)
    if n < 2: 
        return
    logn = ceil(log2(n))
    src, dest = S, [None] * n
    for i in (2**k for k in range(logn)):
        for j in range(0, n, 2*i):
            _merge_iter(src, dest, j, i)
        src, dest = dest, src
        
    if S is not src:
        S[0:n] = src[0:n]
    
    
if __name__ == "__main__":
    S = [4,5,3,2,1]
    # merge_sort(S)
    # print(S)
    # merge_sort(S, desc=True)
    # print(S)
    
    merge_sort_iter(S)
    print(S)
    