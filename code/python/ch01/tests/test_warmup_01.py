"""
Tests for Warmup 01: Sum of Two Numbers
========================================
Chapter 1: The Coder's Toolkit

Run with:
    python -m pytest code/python/ch01/tests/test_warmup_01.py -v
"""

from ch01.practice.warmup_01_sum import solve


def test_sum_positive():
    """1 + 2 should equal 3."""
    assert solve(1, 2) == 3


def test_sum_zeros():
    """0 + 0 should equal 0."""
    assert solve(0, 0) == 0


def test_sum_negative_positive():
    """-5 + 5 should equal 0 (negative and positive cancel out)."""
    assert solve(-5, 5) == 0


def test_sum_large():
    """Large numbers: 1000000 + 2000000 should equal 3000000."""
    assert solve(1000000, 2000000) == 3000000


def test_sum_negatives():
    """Two negatives: -100 + -200 should equal -300."""
    assert solve(-100, -200) == -300
