"""
Tests for Warmup 1: Pair Sum in Sorted Array
==============================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

Run with:
    python -m pytest code/python/ch15/tests/test_warmup_01.py -v
"""
from ch15.practice.warmup_01_pair_sum_sorted import solve


def test_basic():
    assert solve([1, 3, 5, 8, 12, 15], 13) == [1, 12]


def test_first_and_last():
    assert solve([1, 2, 3, 4, 5], 6) == [1, 5]


def test_no_pair():
    assert solve([1, 2, 3, 4, 5], 10) == [-1, -1]


def test_two_elements():
    assert solve([3, 7], 10) == [3, 7]


def test_negatives():
    assert solve([-5, -3, 0, 2, 8], -8) == [-5, -3]


def test_empty():
    assert solve([], 5) == [-1, -1]


def test_single():
    assert solve([5], 5) == [-1, -1]


def test_smallest_first():
    # Multiple valid pairs: [1,9] and [3,7] both sum to 10
    # Return smallest first element: [1, 9]
    assert solve([1, 3, 5, 7, 9], 10) == [1, 9]
