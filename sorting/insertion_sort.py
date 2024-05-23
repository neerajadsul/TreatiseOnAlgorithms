""" Insertion sort inserts j'th element 
to the correct location during j'th iteration.
"""
def insertion_sort_list(S):
    n = len(S)
    if n < 2:
        return
    count = 0
    for i in range(1, n):
        for j in range(i, 0, -1):
            if S[j-1] > S[j]:
               S[j-1], S[j] = S[j], S[j-1] 
            count += 1
    # print(n, count)
    

if __name__ == "__main__":
    # S = [-4, -1, 0, 2, 3, 5]
    import random
    S = [random.random() for _ in range(10_000)]
    insertion_sort_list(S)
    # print(S)