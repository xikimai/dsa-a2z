"""
Tests for Warmup 4: Count Inversions (BIT)
==========================================
Chapter 30: Segment Trees & Range Queries

Run with:
    python -m pytest code/python/ch30/tests/test_warmup_04.py -v
"""
from ch30.practice.warmup_04_count_inversions import solve


def test_mixed():
    assert solve([2, 3, 8, 6, 1]) == 5


def test_reverse_sorted():
    assert solve([5, 4, 3, 2, 1]) == 10


def test_sorted():
    assert solve([1, 2, 3, 4, 5]) == 0


def test_all_same():
    assert solve([1, 1, 1]) == 0


def test_empty():
    assert solve([]) == 0
