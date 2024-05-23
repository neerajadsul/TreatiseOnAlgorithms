import random
import numpy as np
from typing import Collection, Tuple


def display_grid(grid, start=(0,0), goal=(4,4), route=[], stdout=None):
    icons = {0:'  ', 1: '🏢'}  # 1: '█'}
    for nrow, row in enumerate(grid):
        for ncol, col in enumerate(row):
            if (nrow, ncol) == start:
                print('🚘', end='', file=stdout)
            elif (nrow, ncol) == goal:
                print('🏁', end='', file=stdout)
            elif (nrow, ncol) in route:
                print('🚘', end='', file=stdout)
            else:
                print(icons[col], end='', file=stdout)
        print('', file=stdout)


def maze_generator(x=10, y=10, threshold=0.7):
    """Generates a 2D Maze for route finding algorithms.

    Args:
        x (int): horizontal tiles
        y (int): vertical tiles
    """
    grid = np.random.rand(x, y)
    grid[grid > threshold] = 1
    grid[grid <= threshold] = 0
    grid[:, -1] = 1
    return grid

def save_maze_cs50format(grid, filepath):
    NROW, NCOL = len(grid), len(grid[0])
    for nrow, row in enumerate(grid):
        if len(row) != NCOL:
            raise ValueError(f'Non uniform grid, first row len: {NROW}, got row {len(row)} len {len(row)}')

    s = '\n'.join(''.join(map(lambda x: '#' if x == 1 else ' ', row)) for row in grid)
    with open(filepath, 'wt') as fp:
        fp.write(s)


def load_cs50_maze(filepath) -> (Collection, Tuple, Tuple):
    """Loads maze from text file and returns
    
        grid: collection of (x,y) in rows and columns
        start: starting point in the grid
        goal: goal in the grid
    """
    try:
        with open(filepath) as fp:
            maze = fp.readlines()
    except FileNotFoundError as e:
        return e(f'{filepath} does not exist.')
    except IOError as e:
        return e(f'Error opening {filepath}. {e}')
    grid = []
    sym_map = {'#': 1,' ': 0,'A': 0, 'B': 0}
    start, goal = None, None
    for x, line in enumerate(maze):
        row = []
        for y, c in enumerate(line):
            if c == '\n':
                continue
            elif c == 'A':
                start = (x, y)
                row.append(sym_map[c])
            elif c == 'B':
                goal = (x, y)
                row.append(sym_map[c])
            elif c in ('#',' '):
                row.append(sym_map[c])
            else:
                raise ValueError(f'Unknown character "{c}" found in grid.')
        grid.append(tuple(row))
    if start is None or goal is None:
        raise ValueError(f'The maze {filepath} should have 1 start and 1 goal.')
    return tuple(grid), start, goal


def get_start_goal(grid):
    start = input('Start: ')
    start = tuple(map(int, start.split(',')))
    goal = input('Goal: ')
    goal = tuple(map(int, goal.split(',')))
    print(start, goal)


def create_new_maze(x=100, y=100, random_seed=None):
    seed = 0
    if random_seed is not None:
        random.seed(random_seed)
    grid = maze_generator(x, y)
    display_grid(grid)
    save = input('Save maze? (y/N): ')
    if save == 'y':
        save_maze_cs50format(grid, f'cs50_mazes/maze_{x}_{y}_s{seed}.txt')
