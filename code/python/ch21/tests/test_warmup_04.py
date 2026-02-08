"""
Tests for Warmup 4: Search in Linked List
==========================================
Chapter 21: Linked Lists — Pointers and Connections

Run with:
    python -m pytest code/python/ch21/tests/test_warmup_04.py -v
"""
from ch21.practice.warmup_04_search import solve


def test_found():
    assert solve([1, 2, 3, 4, 5], 3) is True


def test_not_found():
    assert solve([1, 2, 3], 7) is False


def test_empty():
    assert solve([], 1) is False


def test_single_found():
    assert solve([5], 5) is True


def test_single_not_found():
    assert solve([5], 3) is False


def test_first_element():
    assert solve([10, 20, 30], 10) is True


def test_last_element():
    assert solve([10, 20, 30], 30) is True
