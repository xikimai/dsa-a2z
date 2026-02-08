"""
Tests for Warmup 2: Remove Duplicates from Sorted Array
=========================================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

Run with:
    python -m pytest code/python/ch15/tests/test_warmup_02.py -v
"""
from ch15.practice.warmup_02_remove_duplicates_sorted import solve


def test_basic():
    assert solve([1, 1, 2]) == [1, 2]


def test_many_duplicates():
    assert solve([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == [0, 1, 2, 3, 4]


def test_no_duplicates():
    assert solve([1, 2, 3]) == [1, 2, 3]


def test_all_same():
    assert solve([5, 5, 5, 5]) == [5]


def test_single():
    assert solve([1]) == [1]


def test_empty():
    assert solve([]) == []


def test_negatives():
    assert solve([-3, -3, -1, 0, 0, 2]) == [-3, -1, 0, 2]
