"""
Tests for Challenge 2: Distinct Values in Range (Offline + BIT)
===============================================================
Chapter 30: Segment Trees & Range Queries

Run with:
    python -m pytest code/python/ch30/tests/test_challenge_02.py -v
"""
from ch30.practice.challenge_02_distinct_in_range import solve


def test_basic():
    assert solve([1, 2, 1, 3, 2, 1], [[0, 5], [0, 2], [3, 5]]) == [3, 2, 3]


def test_all_same():
    assert solve([1, 1, 1], [[0, 2]]) == [1]


def test_all_distinct():
    assert solve([1, 2, 3, 4], [[0, 3], [1, 2]]) == [4, 2]


def test_single():
    assert solve([5], [[0, 0]]) == [1]
