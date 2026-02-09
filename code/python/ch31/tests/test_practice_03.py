"""
Tests for Practice 3: Minimum Score Triangulation of Polygon
=============================================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

Run with:
    python -m pytest code/python/ch31/tests/test_practice_03.py -v
"""
from ch31.practice.practice_03_min_score_triangulation import solve


def test_triangle():
    assert solve([1, 2, 3]) == 6


def test_square():
    assert solve([3, 7, 4, 5]) == 144


def test_hexagon():
    assert solve([1, 3, 1, 4, 1, 5]) == 13


def test_unit_triangle():
    assert solve([1, 1, 1]) == 1
