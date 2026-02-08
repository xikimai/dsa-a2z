"""
Tests for Practice 3: Rat in a Maze
Run with: python -m pytest code/python/ch13/tests/test_practice_03.py -v
"""
from ch13.practice.practice_03_rat_in_maze import solve


def test_basic_4x4():
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]
    ]
    assert solve(maze) == ["DDRDRR", "DRDDRR"]


def test_single_cell():
    assert solve([[1]]) == [""]


def test_no_path():
    maze = [
        [1, 0],
        [0, 1]
    ]
    assert solve(maze) == []


def test_straight_down_right():
    maze = [
        [1, 1],
        [0, 1]
    ]
    assert solve(maze) == ["RD"]


def test_multiple_paths():
    maze = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    result = solve(maze)
    assert len(result) == 12  # All paths in 3x3 open grid
    assert result == sorted(result)  # Should be sorted
