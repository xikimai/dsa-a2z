"""
Tests for Practice 1: Closest Pair of Points
==============================================
Chapter 34: Computational Geometry & Sweep Line

Run with:
    python -m pytest code/python/ch34/tests/test_practice_01.py -v
"""
import math
from ch34.practice.practice_01_closest_pair import solve


def test_basic():
    result = solve([[0, 0], [3, 4], [1, 1], [5, 5]])
    assert abs(result - math.sqrt(2)) < 1e-6


def test_unit_distance():
    result = solve([[0, 0], [1, 0], [0, 1]])
    assert abs(result - 1.0) < 1e-6


def test_two_points():
    result = solve([[0, 0], [10, 10]])
    assert abs(result - math.sqrt(200)) < 1e-6


def test_collinear():
    result = solve([[0, 0], [2, 0], [5, 0]])
    assert abs(result - 2.0) < 1e-6
