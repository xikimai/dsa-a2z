"""
Tests for Warmup 1: Frequency Count
========================================
Chapter 11: Hashing — The Secret Decoder Ring

Run with:
    python -m pytest code/python/ch11/tests/test_warmup_01.py -v
"""
from ch11.practice.warmup_01_frequency_count import solve


def test_basic():
    assert solve([1, 2, 2, 3, 3, 3]) == [[1, 1], [2, 2], [3, 3]]


def test_single():
    assert solve([5]) == [[5, 1]]


def test_empty():
    assert solve([]) == []


def test_unsorted_input():
    assert solve([3, 1, 2, 1]) == [[1, 2], [2, 1], [3, 1]]


def test_all_same():
    assert solve([4, 4, 4, 4]) == [[4, 4]]
