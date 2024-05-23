from itertools import starmap
from multiprocessing import Pool
import concurrent.futures
import glob

from timing import timeit_wrapper
from routing.route_finding import find_route
from routing.maze import load_cs50_maze


@timeit_wrapper
def sequential(inputs):    
    print(f'{"Algo":>5} | {"Time":>5} | {"Route":>6} | {"Visited":>8}')
    n = 0
    for result, exec_time in starmap(timeit_wrapper(find_route), inputs):
        print(f'{inputs[n][3]:>5} | {exec_time:>5.4f} | {len(result[0]): >6} | {len(result[1]):>8}')
        n += 1


@timeit_wrapper
def multiproc_pools(inputs):
    with Pool(10) as p:
        results = p.starmap(find_route, inputs)
    return results


@timeit_wrapper
def concurrent_futures(inputs):
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:        
        maze_solutions = {executor.submit(find_route, *m): n for n, m in enumerate(inputs)}
        for future in concurrent.futures.as_completed(maze_solutions):
            res = maze_solutions[future]
            try:
               results.append(future.result())
            except Exception as exc:
                print(f'{res} caused exception: {exc}')

    return results


if __name__ == "__main__":
    mazes = glob.glob('./benchmarking/assets/mazes/maze_*.txt')
    grids_with_goal = [load_cs50_maze(m) for m in mazes]
    algos = ['bfs', 'gfs', 'dfs']
    
    import itertools
    inputs = tuple(itertools.product(grids_with_goal, algos))
    
    final_inputs = tuple((*x, y) for x, y in inputs)
    results = {}
    results['sequential'] = sequential(inputs=final_inputs)
    results['multiprocessing'] = multiproc_pools(inputs=final_inputs)
    
    results['concurr_futures'] = concurrent_futures(inputs=final_inputs)
    
    import pprint
    pprint(results)