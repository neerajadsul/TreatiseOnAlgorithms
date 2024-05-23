# Experiments based Treatise on Algorithms and Data Structures

![CI Checks](https://github.com/github/TreatiseOnAlgorithms/actions/workflows/python-app.yml/badge.svg)

Experimenting with algorithms is fun and allows deep understanding the
impact of design choices in practical environment.

I explore the implementation with:
Python <img src="./_docs/figures/Python_logo_51.svg.png" height="35px" align="center"> 
and Rust <img src="./_docs/figures/Rust_programming_language_black_logo.svg" height="35px" align="center">


## Route Finding
1. Depth First Search (DFS)
2. Breadth First Search (BFS)
3. Greedy Best-First Search (GBFS)
4. A* Search

## Searching
1. Merge-sort
   - Recursive - Easy to understand and program.
    ```
    %timeit merge_sort([random.random() for _ in range(1000)])
    1.43 ms ± 616 ns per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
    %timeit merge_sort([random.random() for _ in range(10000)])
    19.2 ms ± 17.9 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    %timeit merge_sort([random.random() for _ in range(1_000_000)])
    2.87 s ± 1.87 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    ```
   - iterative - Complicated to program but performant.
    ```
    %timeit merge_sort_iter([random.random() for _ in range(1000)])
    768 µs ± 956 ns per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
    %timeit merge_sort_iter([random.random() for _ in range(10000)])
    10 ms ± 14.5 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    %timeit merge_sort_iter([random.random() for _ in range(1_000_000)])
    1.53 s ± 13.5 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    ```
Note: Benchmark times are on MacBook Pro 16 with M1 Pro.

2. Quick-sort
   - Recursive
   ```
    %timeit quick_sort([random.random() for _ in range(100_000)])
    1.69 s ± 408 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
 

## Adversarial Search
1. Minimax Algorithm