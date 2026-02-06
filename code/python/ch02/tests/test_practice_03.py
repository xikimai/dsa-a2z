"""
Tests for Practice 03: Distance Between Two Points
========================================
Chapter 2: Your First Programs

Run with:
    python -m pytest code/python/ch02/tests/test_practice_03.py -v
"""

import pytest

from ch02.practice.practice_03_distance import solve


def test_three_four_five_triangle():
    """Distance from (0,0) to (3,4) is 5.0 (3-4-5 right triangle)."""
    assert solve(0, 0, 3, 4) == pytest.approx(5.0, abs=1e-4)


def test_same_point():
    """Distance from a point to itself is 0."""
    assert solve(0, 0, 0, 0) == pytest.approx(0.0, abs=1e-4)


def test_another_345():
    """Distance from (1,1) to (4,5) is 5.0."""
    assert solve(1, 1, 4, 5) == pytest.approx(5.0, abs=1e-4)


def test_horizontal_distance():
    """Distance along the x-axis only."""
    assert solve(0, 0, 7, 0) == pytest.approx(7.0, abs=1e-4)


def test_vertical_distance():
    """Distance along the y-axis only."""
    assert solve(0, 0, 0, 3) == pytest.approx(3.0, abs=1e-4)


def test_negative_coordinates():
    """Distance between points with negative coordinates."""
    assert solve(-1, -1, 2, 3) == pytest.approx(5.0, abs=1e-4)
