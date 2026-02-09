"""
Tests for Practice 3: Most Stones Removed
===========================================
Chapter 29: Union-Find & Minimum Spanning Trees

Run with:
    python -m pytest code/python/ch29/tests/test_practice_03.py -v
"""
from ch29.practice.practice_03_most_stones_removed import solve


def test_grid():
    assert solve([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]) == 5


def test_diagonal():
    assert solve([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]) == 3


def test_single():
    assert solve([[0, 0]]) == 0
