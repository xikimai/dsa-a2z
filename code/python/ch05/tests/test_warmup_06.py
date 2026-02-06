"""
Tests for Warmup 6: Move Zeros
========================================
Chapter 5: Collections

Run with:
    python -m pytest code/python/ch05/tests/test_warmup_06.py -v
"""

from ch05.practice.warmup_06_move_zeros import solve


def test_basic_case():
    """Zeros scattered among other numbers."""
    assert solve([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]


def test_zeros_at_start():
    """Zeros at the beginning."""
    assert solve([0, 0, 1]) == [1, 0, 0]


def test_no_zeros():
    """No zeros — list unchanged."""
    assert solve([1, 2, 3]) == [1, 2, 3]


def test_single_zero():
    """Single zero stays."""
    assert solve([0]) == [0]


def test_empty_list():
    """Empty list stays empty."""
    assert solve([]) == []
