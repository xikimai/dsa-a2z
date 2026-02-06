"""
Tests for Warmup 02: Rectangle Area
========================================
Chapter 2: Your First Programs

Run with:
    python -m pytest code/python/ch02/tests/test_warmup_02.py -v
"""

from ch02.practice.warmup_02_rectangle_area import solve


def test_basic_rectangle():
    """5 x 3 rectangle has area 15."""
    assert solve(5, 3) == 15


def test_unit_square():
    """1 x 1 square has area 1."""
    assert solve(1, 1) == 1


def test_large_rectangle():
    """100 x 200 rectangle has area 20000."""
    assert solve(100, 200) == 20000


def test_same_dimensions():
    """10 x 10 square has area 100."""
    assert solve(10, 10) == 100


def test_one_side_is_one():
    """7 x 1 rectangle has area 7."""
    assert solve(7, 1) == 7
