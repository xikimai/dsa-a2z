"""
Tests for Warmup 5: Reverse a Linked List
==========================================
Chapter 21: Linked Lists — Pointers and Connections

Run with:
    python -m pytest code/python/ch21/tests/test_warmup_05.py -v
"""
from ch21.practice.warmup_05_reverse import solve


def test_basic():
    assert solve([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


def test_two_elements():
    assert solve([1, 2]) == [2, 1]


def test_single():
    assert solve([1]) == [1]


def test_empty():
    assert solve([]) == []


def test_already_reversed():
    assert solve([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
