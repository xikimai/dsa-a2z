"""
Tests for Challenge 1: Minimum Height Trees
=============================================
Chapter 28: Topological Sort — Ordering Dependencies

Run with:
    python -m pytest code/python/ch28/tests/test_challenge_01.py -v
"""
from ch28.practice.challenge_01_min_height_trees import solve


def test_star():
    assert sorted(solve(4, [[1, 0], [1, 2], [1, 3]])) == [1]


def test_path():
    assert sorted(solve(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])) == [3, 4]


def test_single():
    assert solve(1, []) == [0]


def test_pair():
    assert sorted(solve(2, [[0, 1]])) == [0, 1]


def test_line():
    assert sorted(solve(4, [[0, 1], [1, 2], [2, 3]])) == [1, 2]
