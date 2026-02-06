"""
Tests for Warmup 05: Sum 1 to N
========================================
Chapter 3: Decisions and Loops

Run with:
    python -m pytest code/python/ch03/tests/test_warmup_05.py -v
"""

from ch03.practice.warmup_05_sum_1_to_n import solve


def test_five():
    """1+2+3+4+5 = 15."""
    assert solve(5) == 15


def test_one():
    """Sum of just 1."""
    assert solve(1) == 1


def test_ten():
    """1+2+...+10 = 55."""
    assert solve(10) == 55


def test_hundred():
    """1+2+...+100 = 5050."""
    assert solve(100) == 5050


def test_zero():
    """Sum of nothing is 0."""
    assert solve(0) == 0
