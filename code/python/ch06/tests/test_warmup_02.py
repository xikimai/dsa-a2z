"""
Tests for Warmup 2: Is It Fast Enough?
========================================
Chapter 6: How Fast Is Your Code?

Run with:
    python -m pytest code/python/ch06/tests/test_warmup_02.py -v
"""

from ch06.practice.warmup_02_fast_enough import solve


def test_n_squared_small():
    """1000^2 = 10^6, well under 10^8."""
    assert solve(1000, "n^2") is True


def test_n_squared_too_big():
    """100000^2 = 10^10, way over 10^8."""
    assert solve(100000, "n^2") is False


def test_n_squared_exact_boundary():
    """10000^2 = 10^8, NOT strictly less than 10^8."""
    assert solve(10000, "n^2") is False


def test_n_squared_just_under():
    """9999^2 = 99980001, just under 10^8."""
    assert solve(9999, "n^2") is True


def test_exponential_large():
    """2^30 ~ 10^9, too big."""
    assert solve(30, "2^n") is False


def test_exponential_small():
    """2^20 ~ 10^6, fast enough."""
    assert solve(20, "2^n") is True


def test_linear():
    """n = 10^6, which is under 10^8."""
    assert solve(1000000, "n") is True


def test_n_log_n():
    """10^6 * log2(10^6) ~ 2*10^7, under 10^8."""
    assert solve(1000000, "n_log_n") is True


def test_constant():
    """O(1) is always 1 operation."""
    assert solve(100000000, "1") is True
