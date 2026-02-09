"""
Tests for Challenge 3: Maximum Subarray Sum in Range (Segment Tree)
===================================================================
Chapter 30: Segment Trees & Range Queries

Run with:
    python -m pytest code/python/ch30/tests/test_challenge_03.py -v
"""
from ch30.practice.challenge_03_max_subarray_range import solve


def test_basic():
    assert solve([1, -2, 3, 4, -1, 2, -5, 3],
                 [[0, 7], [2, 5], [0, 3]]) == [8, 8, 7]


def test_all_negative():
    assert solve([-1, -2, -3], [[0, 2]]) == [-1]


def test_single():
    assert solve([5], [[0, 0]]) == [5]


def test_negative_single():
    assert solve([-5], [[0, 0]]) == [-5]
