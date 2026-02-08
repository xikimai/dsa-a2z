"""
Tests for Challenge 3: Making a Large Island
========================================
Chapter 20: Graphs II — Real Problems

Run with:
    python -m pytest code/python/ch20/tests/test_challenge_03.py -v
"""
from ch20.practice.challenge_03_making_large_island import solve


def test_diagonal():
    assert solve([[1, 0], [0, 1]]) == 3


def test_almost_full():
    assert solve([[1, 1], [1, 0]]) == 4


def test_full():
    assert solve([[1, 1], [1, 1]]) == 4


def test_single_zero():
    assert solve([[0]]) == 1


def test_single_one():
    assert solve([[1]]) == 1


def test_bridge():
    grid = [[1, 0, 1],
            [1, 0, 1],
            [0, 0, 0]]
    # Flipping (0,1) connects left island (size 2) and right island (size 2)
    assert solve(grid) == 5
