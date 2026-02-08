"""
Tests for Warmup 4: Is Array Prefix of Another
=================================================
Chapter 14: Prefix Sums — The Running Total Trick

Run with:
    python -m pytest code/python/ch14/tests/test_warmup_04.py -v
"""
from ch14.practice.warmup_04_is_prefix import solve


def test_is_prefix():
    assert solve([1, 2, 3], [1, 2, 3, 4, 5]) is True


def test_not_prefix():
    assert solve([1, 2, 4], [1, 2, 3, 4, 5]) is False


def test_empty_prefix():
    assert solve([], [1, 2, 3]) is True


def test_equal_arrays():
    assert solve([1, 2, 3], [1, 2, 3]) is True


def test_longer_prefix():
    assert solve([1, 2, 3, 4], [1, 2, 3]) is False


def test_both_empty():
    assert solve([], []) is True


def test_single_match():
    assert solve([7], [7, 8, 9]) is True


def test_single_no_match():
    assert solve([7], [8, 9]) is False
