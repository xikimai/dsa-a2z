"""
Tests for Challenge 2: Shortest Bridge
========================================
Chapter 20: Graphs II — Real Problems

Run with:
    python -m pytest code/python/ch20/tests/test_challenge_02.py -v
"""
from ch20.practice.challenge_02_shortest_bridge import solve


def test_diagonal():
    assert solve([[0, 1], [1, 0]]) == 1


def test_separated():
    assert solve([[0, 1, 0], [0, 0, 0], [0, 0, 1]]) == 2


def test_concentric():
    grid = [[1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]]
    assert solve(grid) == 1


def test_adjacent():
    grid = [[1, 0, 0],
            [0, 0, 0],
            [0, 0, 1]]
    assert solve(grid) == 3


def test_close():
    grid = [[0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 1, 0]]
    assert solve(grid) == 2
