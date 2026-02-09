"""
Tests for Challenge 4: Interval Scheduling
===========================================
Chapter 30: Segment Trees & Range Queries

Run with:
    python -m pytest code/python/ch30/tests/test_challenge_04.py -v
"""
from ch30.practice.challenge_04_interval_scheduling import solve


def test_overlapping():
    assert solve([[1, 3], [2, 5], [4, 7], [6, 9]]) == 2


def test_non_overlapping():
    assert solve([[1, 2], [2, 3], [3, 4], [4, 5]]) == 4


def test_one_large():
    assert solve([[1, 10], [2, 3], [4, 5], [6, 7]]) == 3


def test_single():
    assert solve([[1, 5]]) == 1


def test_empty():
    assert solve([]) == 0
