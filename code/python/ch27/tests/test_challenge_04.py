"""
Tests for Challenge 4: Path with Maximum Minimum Value
=======================================================
Chapter 27: Shortest Paths — Finding the Best Route

Run with:
    python -m pytest code/python/ch27/tests/test_challenge_04.py -v
"""
from ch27.practice.challenge_04_max_min_path import solve


def test_basic():
    assert solve([[5,4,5],[1,2,6],[7,4,6]]) == 4


def test_narrow():
    assert solve([[2,2,1,2,2,2],[1,2,2,2,1,2]]) == 2


def test_larger():
    grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],
            [3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
    assert solve(grid) == 3


def test_single_cell():
    assert solve([[7]]) == 7
