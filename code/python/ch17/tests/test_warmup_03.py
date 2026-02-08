"""
Tests for Warmup 3: Last Stone Weight
=========================================
Chapter 17: Heaps & Priority Queues — The VIP Line

Run with:
    python -m pytest code/python/ch17/tests/test_warmup_03.py -v
"""
from ch17.practice.warmup_03_last_stone_weight import solve


def test_basic():
    assert solve([2, 7, 4, 1, 8, 1]) == 1


def test_single_stone():
    assert solve([1]) == 1


def test_two_equal():
    assert solve([3, 3]) == 0


def test_two_different():
    assert solve([3, 7]) == 4


def test_all_equal():
    assert solve([5, 5, 5, 5]) == 0


def test_descending():
    assert solve([10, 4, 2, 10]) == 2
