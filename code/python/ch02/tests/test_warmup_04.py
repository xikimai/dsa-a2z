"""
Tests for Warmup 04: Swap Two Numbers
========================================
Chapter 2: Your First Programs

Run with:
    python -m pytest code/python/ch02/tests/test_warmup_04.py -v
"""

from ch02.practice.warmup_04_swap import solve


def test_swap_positive():
    """Swapping 3 and 7 gives (7, 3)."""
    assert solve(3, 7) == (7, 3)


def test_swap_zeros():
    """Swapping 0 and 0 gives (0, 0)."""
    assert solve(0, 0) == (0, 0)


def test_swap_negative_positive():
    """Swapping -1 and 1 gives (1, -1)."""
    assert solve(-1, 1) == (1, -1)


def test_swap_same_values():
    """Swapping identical values gives the same values."""
    assert solve(5, 5) == (5, 5)


def test_swap_large_numbers():
    """Swapping large numbers works correctly."""
    assert solve(1000000, -999999) == (-999999, 1000000)
