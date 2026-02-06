"""
Tests for Warmup 1: Count the Steps
========================================
Chapter 6: How Fast Is Your Code?

Run with:
    python -m pytest code/python/ch06/tests/test_warmup_01.py -v
"""

from ch06.practice.warmup_01_count_steps import solve


def test_single_loop():
    """Single loop: n iterations."""
    assert solve("single_loop", 100) == 100


def test_double_loop():
    """Double loop: n * n iterations."""
    assert solve("double_loop", 10) == 100


def test_half_loop_even():
    """Half loop with even n."""
    assert solve("half_loop", 100) == 50


def test_half_loop_odd():
    """Half loop with odd n (floor division)."""
    assert solve("half_loop", 7) == 3


def test_dependent_loop():
    """Dependent loop: n*(n+1)//2."""
    assert solve("dependent_loop", 4) == 10


def test_log_loop_power_of_two():
    """Log loop with a power of 2."""
    assert solve("log_loop", 16) == 4


def test_log_loop_one():
    """Log loop with n=1 should be 0."""
    assert solve("log_loop", 1) == 0


def test_log_loop_large():
    """Log loop with n=1024 should be 10."""
    assert solve("log_loop", 1024) == 10
