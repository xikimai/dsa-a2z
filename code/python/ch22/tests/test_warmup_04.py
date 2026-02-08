"""
Tests for Warmup 4: Next Greater Element
============================================
Chapter 22: Stacks & Queues — Order Matters

Run with:
    python -m pytest code/python/ch22/tests/test_warmup_04.py -v
"""
from ch22.practice.warmup_04_next_greater_element import solve


def test_basic():
    assert solve([4, 5, 2, 10, 8]) == [5, 10, 10, -1, -1]


def test_decreasing():
    assert solve([3, 2, 1]) == [-1, -1, -1]


def test_increasing():
    assert solve([1, 2, 3]) == [2, 3, -1]


def test_single():
    assert solve([5]) == [-1]


def test_empty():
    assert solve([]) == []


def test_duplicates():
    assert solve([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]


def test_all_same():
    assert solve([3, 3, 3]) == [-1, -1, -1]
