"""
Tests for Practice 3: Sliding Window Maximum
================================================
Chapter 22: Stacks & Queues — Order Matters

Run with:
    python -m pytest code/python/ch22/tests/test_practice_03.py -v
"""
from ch22.practice.practice_03_sliding_window_max import solve


def test_basic():
    assert solve([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]


def test_single_element():
    assert solve([1], 1) == [1]


def test_k_equals_n():
    assert solve([1, 3, 2], 3) == [3]


def test_all_same():
    assert solve([5, 5, 5, 5], 2) == [5, 5, 5]


def test_decreasing():
    assert solve([9, 7, 5, 3, 1], 3) == [9, 7, 5]


def test_increasing():
    assert solve([1, 2, 3, 4, 5], 2) == [2, 3, 4, 5]


def test_k_one():
    assert solve([4, 2, 7, 1], 1) == [4, 2, 7, 1]
