import pytest
import logging

from routing.route_finding import find_route, greedy_first_heuristics
from routing.maze import display_grid

logger = logging.getLogger()


@pytest.fixture
def maze_goal():
    grid_1 = (
        (0, 1, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0),
        (0, 1, 0, 1, 0, 0),
        (0, 1, 0, 0, 0, 1),
        (0, 0, 0, 1, 0, 0),
        (1, 0, 0, 1, 0, 1),
    )
    start = (0, 0)
    goal = (5, 4)
    return grid_1, start, goal


def test_route_finding_depth_first(maze_goal):
    maze, start, goal = maze_goal
    algo = 'dfs'
    route, visited = find_route(maze, start, goal, algorithm=algo)
    assert route is not None
    # with open(f'{algo}_result.txt', 'w') as fp:
        # display_grid(maze, start, goal=goal, route=route, stdout=fp)


def test_route_finding_breadth_first(maze_goal):
    maze, start, goal = maze_goal
    algo = 'bfs'
    route, visited = find_route(maze, start, goal, algorithm=algo)
    assert route is not None
    # with open(f'{algo}_result.txt', 'w') as fp:
        # display_grid(maze, start, goal=goal, route=route, stdout=fp)


def test_route_finding_greedy_first(maze_goal):
    maze, start, goal = maze_goal
    algo = 'gfs'
    route, visited = find_route(maze, start, goal,
                                algorithm=algo, heuristics=greedy_first_heuristics)
    assert route is not None
    # with open(f'{algo}_result.txt', 'w') as fp:
        # display_grid(maze, start, goal=goal, route=route, stdout=fp)
