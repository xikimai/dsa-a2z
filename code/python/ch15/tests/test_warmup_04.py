"""
Tests for Warmup 4: Move Zeros to End
=======================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

Run with:
    python -m pytest code/python/ch15/tests/test_warmup_04.py -v
"""
from ch15.practice.warmup_04_move_zeros import solve


def test_basic():
    assert solve([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]


def test_single_zero():
    assert solve([0]) == [0]


def test_no_zeros():
    assert solve([1, 2, 3]) == [1, 2, 3]


def test_all_zeros():
    assert solve([0, 0, 0]) == [0, 0, 0]


def test_zeros_at_end():
    assert solve([1, 2, 0, 0]) == [1, 2, 0, 0]


def test_zeros_at_start():
    assert solve([0, 0, 1]) == [1, 0, 0]


def test_empty():
    assert solve([]) == []


def test_mixed():
    assert solve([0, 5, 0, 3, 0, 1]) == [5, 3, 1, 0, 0, 0]
