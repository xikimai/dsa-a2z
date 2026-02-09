"""
Tests for Challenge 1: Convex Hull Perimeter
=============================================
Chapter 34: Computational Geometry & Sweep Line

Run with:
    python -m pytest code/python/ch34/tests/test_challenge_01.py -v
"""
import math
from ch34.practice.challenge_01_hull_perimeter import solve


def test_rectangle():
    result = solve([[0, 0], [4, 0], [4, 3], [0, 3], [2, 1]])
    assert abs(result - 14.0) < 1e-6


def test_triangle():
    result = solve([[0, 0], [1, 0], [0, 1]])
    expected = 2 + math.sqrt(2)
    assert abs(result - expected) < 1e-6


def test_single_point():
    result = solve([[5, 5]])
    assert abs(result - 0.0) < 1e-6


def test_two_points():
    result = solve([[0, 0], [3, 4]])
    assert abs(result - 10.0) < 1e-6  # 2 * 5.0
