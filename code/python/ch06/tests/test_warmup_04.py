"""
Tests for Warmup 4: Sum of 1 to N
========================================
Chapter 6: How Fast Is Your Code?

Run with:
    python -m pytest code/python/ch06/tests/test_warmup_04.py -v
"""

from ch06.practice.warmup_04_sum_to_n import solve


def test_ten():
    """Sum of 1..10 = 55 by all three methods."""
    assert solve(10) == [55, 55, 55]


def test_one():
    """Sum of 1..1 = 1."""
    assert solve(1) == [1, 1, 1]


def test_hundred():
    """Sum of 1..100 = 5050."""
    assert solve(100) == [5050, 5050, 5050]


def test_zero():
    """Sum of nothing = 0."""
    assert solve(0) == [0, 0, 0]
