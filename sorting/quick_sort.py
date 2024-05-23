"""Quick sort is like a balance, 
    - choose pivot, 
    - put smaller items in left bucket, 
    - larger item in right bucket
    - equal to pivot in middle bucket.
Then recusively sort each bucket.
At the end, combine the buckets together as left + middle + right.
"""

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
    
    
if __name__ == "__main__":
    S = [4, -2, 3, 0, -6]
    quick_sort_lists(S)
    print(S)
