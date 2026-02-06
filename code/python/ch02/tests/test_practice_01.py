"""
Tests for Practice 01: Circle Properties
========================================
Chapter 2: Your First Programs

Run with:
    python -m pytest code/python/ch02/tests/test_practice_01.py -v
"""

import math

import pytest

from ch02.practice.practice_01_circle import solve


def test_unit_circle():
    """Unit circle (radius=1): area=pi, circumference=2*pi."""
    area, circ = solve(1.0)
    assert area == pytest.approx(math.pi, abs=1e-4)
    assert circ == pytest.approx(2 * math.pi, abs=1e-4)


def test_radius_five():
    """Circle with radius 5."""
    area, circ = solve(5.0)
    assert area == pytest.approx(78.5398, abs=1e-4)
    assert circ == pytest.approx(31.4159, abs=1e-4)


def test_radius_ten():
    """Circle with radius 10."""
    area, circ = solve(10.0)
    assert area == pytest.approx(314.1593, abs=1e-4)
    assert circ == pytest.approx(62.8319, abs=1e-4)


def test_small_radius():
    """Circle with a small radius of 0.5."""
    area, circ = solve(0.5)
    assert area == pytest.approx(0.7854, abs=1e-4)
    assert circ == pytest.approx(3.1416, abs=1e-4)


def test_large_radius():
    """Circle with radius 100."""
    area, circ = solve(100.0)
    assert area == pytest.approx(31415.9265, abs=1e-2)
    assert circ == pytest.approx(628.3185, abs=1e-4)
