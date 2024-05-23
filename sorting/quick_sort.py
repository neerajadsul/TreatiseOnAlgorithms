"""Quick sort is like a balance, 
    - choose pivot, 
    - put smaller items in left bucket, 
    - larger item in right bucket
    - equal to pivot in middle bucket.
Then recusively sort each bucket.
At the end, combine the buckets together as left + middle + right.
"""
from queue import deque
from typing import Deque


def quick_sort_lists(S):
    n = len(S)
    if n < 2:
        return

    pivot = S[-1]
    left, middle, right = [], [], []
    
    while len(S) > 0:
        num = S.pop()
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            middle.append(num)
            
    quick_sort_lists(left)
    quick_sort_lists(right)
    
    while len(left) > 0:
        S.append(left.pop(0))
    while len(middle) > 0:
        S.append(middle.pop(0))
    while len(right) > 0:
        S.append(right.pop(0))
    

def quick_sort_deque(S: Deque):
    if not isinstance(S, Deque):
        raise ValueError('Expected sequence of Deque type')
    n = len(S)
    if n < 2:
        return
        
    pivot = S.pop()
    
    lower, middle, higher = deque(), deque(), deque()
    middle.append(pivot)
    
    while len(S) > 0:
        m = S.pop()
        if m < pivot:
            lower.append(m)
        elif m > pivot:
            higher.append(m)
        else:
            middle.append(m)
    
    quick_sort_deque(lower)
    quick_sort_deque(higher)
    
    while len(lower) > 0:
        S.append(lower.popleft())
    while len(middle) > 0:
        S.append(middle.popleft())
    while len(higher) > 0:
        S.append(higher.popleft())
    
   
    
if __name__ == "__main__":
    S = [4, -2, 3, 0, -6]
    quick_sort_lists(S)
    print(S)

    S = deque([4, -2, 3, 0, -6])
    quick_sort_deque(S)
    print(S)