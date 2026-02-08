"""
Tests for Challenge 3: Online Stock Span
============================================
Chapter 22: Stacks & Queues — Order Matters

Run with:
    python -m pytest code/python/ch22/tests/test_challenge_03.py -v
"""
from ch22.practice.challenge_03_online_stock_span import solve


def test_basic():
    assert solve([100, 80, 60, 70, 60, 75, 85]) == [1, 1, 1, 2, 1, 4, 6]


def test_increasing():
    assert solve([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_decreasing():
    assert solve([5, 4, 3, 2, 1]) == [1, 1, 1, 1, 1]


def test_all_same():
    assert solve([5, 5, 5, 5]) == [1, 2, 3, 4]


def test_single():
    assert solve([10]) == [1]


def test_two_elements():
    assert solve([10, 20]) == [1, 2]
