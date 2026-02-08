"""
Tests for Warmup 2: Highest and Lowest Frequency Element
========================================
Chapter 11: Hashing — The Secret Decoder Ring

Run with:
    python -m pytest code/python/ch11/tests/test_warmup_02.py -v
"""
from ch11.practice.warmup_02_highest_lowest_freq import solve


def test_basic():
    assert solve([1, 2, 2, 3, 3, 3]) == [3, 1]


def test_three_freqs():
    assert solve([10, 10, 10, 20, 20, 30]) == [10, 30]


def test_single():
    assert solve([5]) == [5, 5]


def test_four_elements():
    assert solve([1, 1, 2, 2, 2, 2, 3, 3, 3]) == [2, 1]


def test_ascending_freq():
    assert solve([7, 7, 8, 8, 8, 9, 9, 9, 9]) == [9, 7]
