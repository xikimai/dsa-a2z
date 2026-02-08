"""
Tests for Challenge 4: Minimum Operations to Make All Elements Equal
======================================================================
Chapter 14: Prefix Sums — The Running Total Trick

Run with:
    python -m pytest code/python/ch14/tests/test_challenge_04.py -v
"""
from ch14.practice.challenge_04_min_ops_make_equal import solve


def test_basic():
    assert solve([1, 2, 3]) == 2


def test_single():
    assert solve([5]) == 0


def test_already_equal():
    assert solve([3, 3, 3]) == 0


def test_two_elements():
    assert solve([1, 5]) == 4


def test_larger():
    assert solve([1, 2, 9, 10]) == 16


def test_negatives():
    assert solve([-5, -3, -1]) == 4


def test_spread():
    assert solve([1, 100]) == 99
