"""
Tests for Practice 2: Path with Minimum Effort
================================================
Chapter 27: Shortest Paths — Finding the Best Route

Run with:
    python -m pytest code/python/ch27/tests/test_practice_02.py -v
"""
from ch27.practice.practice_02_min_effort import solve


def test_basic():
    assert solve([[1,2,2],[3,8,2],[5,3,5]]) == 2


def test_small_diff():
    assert solve([[1,2,3],[3,8,4],[5,3,5]]) == 1


def test_zero_effort():
    grid = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
    assert solve(grid) == 0


def test_single_cell():
    assert solve([[5]]) == 0


def test_flat():
    assert solve([[3,3],[3,3]]) == 0
