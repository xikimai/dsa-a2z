"""
Tests for Warmup 4: Check If Sorted
========================================
Chapter 8: The Art of Sorting — Putting Things in Order

Run with:
    python -m pytest code/python/ch08/tests/test_warmup_04.py -v
"""

from ch08.practice.warmup_04_check_if_sorted import solve


def test_sorted():
    assert solve([1, 2, 3, 4, 5]) == True


def test_unsorted():
    assert solve([1, 3, 2, 4, 5]) == False


def test_empty():
    assert solve([]) == True


def test_single():
    assert solve([7]) == True


def test_all_equal():
    assert solve([1, 1, 1]) == True
