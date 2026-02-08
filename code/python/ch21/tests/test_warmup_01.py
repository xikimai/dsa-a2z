"""
Tests for Warmup 1: Traverse Linked List
==========================================
Chapter 21: Linked Lists — Pointers and Connections

Run with:
    python -m pytest code/python/ch21/tests/test_warmup_01.py -v
"""
from ch21.practice.warmup_01_traverse import solve


def test_basic():
    assert solve([1, 2, 3]) == [1, 2, 3]


def test_single():
    assert solve([5]) == [5]


def test_empty():
    assert solve([]) == []


def test_five_elements():
    assert solve([10, 20, 30, 40, 50]) == [10, 20, 30, 40, 50]


def test_negative():
    assert solve([-1, -2, -3]) == [-1, -2, -3]
