"""
Tests for Challenge 1: Range Update Range Query (Set, Lazy Segment Tree)
========================================================================
Chapter 30: Segment Trees & Range Queries

Run with:
    python -m pytest code/python/ch30/tests/test_challenge_01.py -v
"""
from ch30.practice.challenge_01_range_update_query import solve


def test_basic():
    assert solve(5, [[1, 0, 4, 3], [2, 0, 4], [1, 1, 3, 5], [2, 0, 4]]) == [15, 21]


def test_overwrite():
    assert solve(3, [[1, 0, 2, 10], [2, 0, 2], [1, 1, 1, 0], [2, 0, 2]]) == [30, 20]


def test_single():
    assert solve(1, [[1, 0, 0, 7], [2, 0, 0], [1, 0, 0, 3], [2, 0, 0]]) == [7, 3]
