"""
Tests for Challenge 3: Sliding Window Maximum
=================================================
Chapter 17: Heaps & Priority Queues — The VIP Line

Run with:
    python -m pytest code/python/ch17/tests/test_challenge_03.py -v
"""
from ch17.practice.challenge_03_sliding_window_max import solve


def test_basic():
    assert solve([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]


def test_single():
    assert solve([1], 1) == [1]


def test_k_equals_n():
    assert solve([1, -1], 2) == [1]


def test_ascending():
    assert solve([1, 2, 3, 4, 5], 3) == [3, 4, 5]


def test_descending():
    assert solve([5, 4, 3, 2, 1], 3) == [5, 4, 3]


def test_all_same():
    assert solve([2, 2, 2, 2], 2) == [2, 2, 2]


def test_window_1():
    assert solve([4, 3, 5, 4, 2], 1) == [4, 3, 5, 4, 2]
