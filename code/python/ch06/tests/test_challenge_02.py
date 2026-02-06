"""
Tests for Challenge 2: Performance Showdown
========================================
Chapter 6: How Fast Is Your Code?

Run with:
    python -m pytest code/python/ch06/tests/test_challenge_02.py -v
"""

from ch06.practice.challenge_02_performance_showdown import solve


def test_quadratic_vs_nlogn():
    """n^2 is slower than n_log_n for large n."""
    assert solve("n^2", "n_log_n", 1000) == "B"


def test_tie():
    """Same complexity at same n -> TIE."""
    assert solve("n", "n", 100) == "TIE"


def test_constant_vs_log():
    """O(1) always beats O(log n)."""
    assert solve("1", "log_n", 1000000) == "A"


def test_quadratic_vs_cubic():
    """n^2 < n^3 for n > 1."""
    assert solve("n^2", "n^3", 10) == "A"


def test_nlogn_vs_quadratic():
    """n log n beats n^2."""
    assert solve("n_log_n", "n^2", 100) == "A"
