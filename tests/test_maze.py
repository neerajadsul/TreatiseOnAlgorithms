import pytest

from routing.maze import maze_generator


def test_maze_generator():
    x, y = 9, 9
    maze = maze_generator(x, y, threshold=0.0)
    assert sum([sum(m) for m in maze]) == (x*y)
    maze = maze_generator(x, y, threshold=1.0)
    assert sum([sum(m) for m in maze]) == 0
    threshold=0.5
    maze = maze_generator(x, y, threshold=threshold)
    assert sum([sum(m) for m in maze])/(x*y) <= (threshold+0.1)
    threshold=0.7
    maze = maze_generator(x, y, threshold=threshold)
    assert sum([sum(m) for m in maze])/(x*y) <= (threshold+0.1)
    
    

def test_load_maze():
    """Tests loading a 2-D maze from a text file."""
    pass


def test_save_maze_as_text():
    """Test saving 2-D maze in a text file.
    """
    pass


def test_save_maze_as_binary():
    """Test saving 2-D maze in a binary file.
    """
    pass

def test_next_moves_given_current_position():
    """Test getting next possible moves in a maze given current position.
    """
    pass