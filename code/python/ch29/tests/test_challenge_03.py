"""
Tests for Challenge 3: Number of Islands II
=============================================
Chapter 29: Union-Find & Minimum Spanning Trees

Run with:
    python -m pytest code/python/ch29/tests/test_challenge_03.py -v
"""
from ch29.practice.challenge_03_islands_ii import solve


def test_basic():
    assert solve(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]) == [1, 1, 2, 3]


def test_single():
    assert solve(1, 1, [[0, 0]]) == [1]
