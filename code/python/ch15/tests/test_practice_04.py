"""
Tests for Practice 4: Subarray Sum Equals K (Sliding Window)
==============================================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

Run with:
    python -m pytest code/python/ch15/tests/test_practice_04.py -v
"""
from ch15.practice.practice_04_subarray_sum_equals_k import solve


def test_basic():
    assert solve([1, 1, 1], 2) == 2


def test_exact():
    assert solve([1, 2, 3], 3) == 2


def test_single_match():
    assert solve([5], 5) == 1


def test_no_match():
    assert solve([1, 2, 3], 10) == 0


def test_all_ones():
    assert solve([1, 1, 1, 1, 1], 3) == 3


def test_larger():
    assert solve([2, 3, 1, 2, 4, 3], 7) == 2
