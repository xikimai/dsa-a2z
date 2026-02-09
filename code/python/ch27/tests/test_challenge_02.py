"""
Tests for Challenge 2: Shortest Path with Alternating Colors
=============================================================
Chapter 27: Shortest Paths — Finding the Best Route

Run with:
    python -m pytest code/python/ch27/tests/test_challenge_02.py -v
"""
from ch27.practice.challenge_02_alternating_colors import solve


def test_red_only():
    assert solve(3, [[0,1],[1,2]], []) == [0, 1, -1]


def test_mixed():
    assert solve(3, [[0,1]], [[2,1]]) == [0, 1, -1]


def test_both_colors():
    assert solve(3, [[0,1],[0,2]], [[1,0]]) == [0, 1, 1]


def test_single_node():
    assert solve(1, [], []) == [0]
