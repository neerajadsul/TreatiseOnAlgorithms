import time

from .maze import load_cs50_maze
from typing import List, Any


def next_pos(grid, node):
    N = (-1, 0)
    S = (1, 0)
    E = (0, 1)
    W = (0, -1)
    positions = []
    for d in [N, S, E, W]:
        try:
            x, y = max(0, node.loc[0] + d[0]), max(0, node.loc[1] + d[1])
            p = grid[x][y]
        except IndexError:
            continue
        else:
            if p == 0 and (x, y) != node.loc:
                positions.append((x, y))
    return positions


class Node:
    def __init__(self, loc, parent):
        self.loc = loc
        self.parent = parent

    def __eq__(self, other):
        return self.loc == other.loc

    def __repr__(self):
        return self.loc

    def __str__(self):
        return f'{self.loc}'


def manhattan_distance(n1, n2):
    x1, y1 = n1
    x2, y2 = n2

    return abs(y2 - y1) + abs(x2 - x1)


def no_heuristic(turns, goal):
    return turns


def greedy_first_heuristics(turns, goal):
    mhat_distances = [manhattan_distance(turn, goal) for turn in turns]
    turns = tuple(sorted(zip(mhat_distances, turns), reverse=True))
    return turns


def find_route(grid, start, goal, algorithm='bfs') -> (List, Any):
    """[summary]

    Args:
        grid: search grid with each point as (x,y)
        start: starting point
        goal: goal point
        algorithm: type of search algorithm, 'bfs', 'dfs' or 'gfs'
        heuristics: heuristic function

    Returns:
        route: list of nodes reachable from start and goal
        visited: set of nodes visited during search
    """
    first_or_last = {'dfs': -1, 'bfs': 0, 'gfs': 0}
    if algorithm not in first_or_last.keys():
        raise ValueError(f'Invalid algorithm choice: {algorithm}')

    start_node = Node(start, None)
    visited = set()
    route = list()
    route.append(start_node)

    while True:

        if len(route) == 0:
            return None, visited

        node = route.pop(first_or_last[algorithm])
        visited.add(node.loc)

        if node == Node(goal, None):
            full_route = []
            while node.parent is not None:
                full_route.append(node.loc)
                node = node.parent
            full_route.append(start_node.loc)
            return list(reversed(full_route)), visited

        turns = next_pos(grid, node)
        if algorithm == 'gfs':
            mhat_distances = [(manhattan_distance(turn, goal), turn) for turn in turns]
            mhat_distances.sort(reverse=True)
            turns = [x[1] for x in mhat_distances]

        for turn in turns:
            if turn not in visited and Node(turn, None) not in route:
                route.append(Node(turn, parent=node))


def cs50_routes(func, maze, algo=None):
    grid, start, goal = load_cs50_maze(f'./{maze}')
    begin = time.time()
    route, visited = func(grid, start=start, goal=goal)
    finish = time.time()
    return (f'{algo = }, {len(route) = }, {len(visited) = }, {finish - begin: 0.5f}')
