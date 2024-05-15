"""Merge sort is divide-and-conquer sorting technique.
Implemented as in-place sort.
Split the sequence in two halves S1 and S2, 
Sort each half S1 and S2 recusively.
Merge two halves S1 and S2 into S
"""
from operator import lt, gt

def merge(S1, S2, S, desc):
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
    merge(S1, S2, S, desc=desc)
            
    
if __name__ == "__main__":
    S = [4,5,3,2,1]
    merge_sort(S)
    print(S)
    merge_sort(S, desc=True)
    print(S)
    