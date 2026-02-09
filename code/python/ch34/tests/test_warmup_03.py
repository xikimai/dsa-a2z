"""
Tests for Warmup 3: Polygon Area (Shoelace Formula)
=====================================================
Chapter 34: Computational Geometry & Sweep Line

Run with:
    python -m pytest code/python/ch34/tests/test_warmup_03.py -v
"""
from ch34.practice.warmup_03_polygon_area import solve


def test_rectangle():
    assert abs(solve([[0, 0], [4, 0], [4, 3], [0, 3]]) - 12.0) < 1e-6


def test_triangle():
    assert abs(solve([[0, 0], [1, 0], [0, 1]]) - 0.5) < 1e-6


def test_square():
    assert abs(solve([[0, 0], [2, 0], [2, 2], [0, 2]]) - 4.0) < 1e-6


def test_reverse_order():
    # Reversed order should give same area (absolute value)
    assert abs(solve([[0, 3], [4, 3], [4, 0], [0, 0]]) - 12.0) < 1e-6
