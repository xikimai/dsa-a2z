"""
Tests for Practice 4: Find Median from Data Stream
======================================================
Chapter 17: Heaps & Priority Queues — The VIP Line

Run with:
    python -m pytest code/python/ch17/tests/test_practice_04.py -v
"""
from ch17.practice.practice_04_find_median import solve


def test_basic():
    assert solve([5, 15, 1, 3]) == [5.0, 10.0, 5.0, 4.0]


def test_ascending():
    assert solve([2, 3, 4]) == [2.0, 2.5, 3.0]


def test_single():
    assert solve([1]) == [1.0]


def test_two():
    assert solve([1, 2]) == [1.0, 1.5]


def test_descending():
    assert solve([5, 4, 3, 2, 1]) == [5.0, 4.5, 4.0, 3.5, 3.0]


def test_all_same():
    assert solve([7, 7, 7, 7]) == [7.0, 7.0, 7.0, 7.0]


def test_negative():
    assert solve([-1, -2, -3]) == [-1.0, -1.5, -2.0]
