"""
Tests for Warmup 2: Convex Hull
================================
Chapter 34: Computational Geometry & Sweep Line

Run with:
    python -m pytest code/python/ch34/tests/test_warmup_02.py -v
"""
from ch34.practice.warmup_02_convex_hull import solve


def test_square_with_interior():
    result = solve([[0, 0], [2, 0], [0, 2], [2, 2], [1, 1]])
    assert result == [[0, 0], [2, 0], [2, 2], [0, 2]]


def test_collinear_points():
    result = solve([[0, 0], [1, 0], [2, 0]])
    assert result == [[0, 0], [2, 0]]


def test_triangle():
    result = solve([[0, 0], [4, 0], [2, 3]])
    assert result == [[0, 0], [4, 0], [2, 3]]


def test_single_point():
    result = solve([[5, 5]])
    assert result == [[5, 5]]


def test_duplicate_points():
    result = solve([[0, 0], [0, 0], [1, 0], [1, 0], [0, 1]])
    assert result == [[0, 0], [1, 0], [0, 1]]
