"""
Tests for Warmup 1: Kth Largest Element
==========================================
Chapter 17: Heaps & Priority Queues — The VIP Line

Run with:
    python -m pytest code/python/ch17/tests/test_warmup_01.py -v
"""
from ch17.practice.warmup_01_kth_largest import solve


def test_basic():
    assert solve([3, 2, 1, 5, 6, 4], 2) == 5


def test_with_duplicates():
    assert solve([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


def test_k_equals_1():
    assert solve([1], 1) == 1


def test_k_equals_n():
    assert solve([7, 6, 5, 4, 3, 2, 1], 7) == 1


def test_all_same():
    assert solve([5, 5, 5, 5], 2) == 5


def test_negative_numbers():
    assert solve([-1, -2, -3, -4, -5], 2) == -2


def test_mixed():
    assert solve([3, -2, 7, 1, 0, -5], 3) == 1
