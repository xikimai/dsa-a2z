"""
Tests for Warmup 3: Mystery Complexity
========================================
Chapter 6: How Fast Is Your Code?

Run with:
    python -m pytest code/python/ch06/tests/test_warmup_03.py -v
"""

from ch06.practice.warmup_03_mystery_complexity import solve


def test_constant():
    """All counts the same -> O(1)."""
    assert solve([1, 10, 100, 1000], [5, 5, 5, 5]) == "O(1)"


def test_logarithmic():
    """Count increases by 1 when n doubles -> O(log n)."""
    assert solve([1, 2, 4, 8, 16], [0, 1, 2, 3, 4]) == "O(log n)"


def test_linear():
    """Count doubles when n doubles -> O(n)."""
    assert solve([100, 200, 400, 800], [100, 200, 400, 800]) == "O(n)"


def test_quadratic():
    """Count quadruples when n doubles -> O(n^2)."""
    assert solve([10, 20, 40, 80], [100, 400, 1600, 6400]) == "O(n^2)"


def test_linear_short():
    """Shorter input, still linear."""
    assert solve([1000, 2000, 4000], [1000, 2000, 4000]) == "O(n)"
