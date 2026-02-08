"""
Tests for Practice 2: Merge K Sorted Arrays
===============================================
Chapter 17: Heaps & Priority Queues — The VIP Line

Run with:
    python -m pytest code/python/ch17/tests/test_practice_02.py -v
"""
from ch17.practice.practice_02_merge_k_sorted import solve


def test_three_arrays():
    assert solve([[1, 4, 7], [2, 5, 8], [3, 6, 9]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_two_arrays():
    assert solve([[1, 3, 5], [2, 4, 6]]) == [1, 2, 3, 4, 5, 6]


def test_with_empty():
    assert solve([[], [1]]) == [1]


def test_all_empty():
    assert solve([[], []]) == []


def test_single_array():
    assert solve([[1, 2, 3]]) == [1, 2, 3]


def test_empty_input():
    assert solve([]) == []


def test_overlapping():
    assert solve([[1, 3, 5], [1, 2, 6], [2, 4, 8]]) == [1, 1, 2, 2, 3, 4, 5, 6, 8]
