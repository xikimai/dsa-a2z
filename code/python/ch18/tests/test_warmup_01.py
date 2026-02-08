"""
Tests for Warmup 1: Assign Cookies
=====================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

Run with:
    python -m pytest code/python/ch18/tests/test_warmup_01.py -v
"""
from ch18.practice.warmup_01_assign_cookies import solve


def test_basic():
    assert solve([1, 2, 3], [1, 1]) == 1


def test_all_satisfied():
    assert solve([1, 2], [1, 2, 3]) == 2


def test_none_satisfied():
    assert solve([10, 9, 8, 7], [1, 2, 3, 4]) == 0


def test_partial():
    assert solve([10, 9, 8, 7], [5, 6, 7, 8]) == 2


def test_empty_children():
    assert solve([], [1, 2, 3]) == 0


def test_empty_cookies():
    assert solve([1, 2], []) == 0


def test_single():
    assert solve([1], [1]) == 1


def test_large_greed():
    assert solve([1, 2, 3], [3]) == 1
