"""
Tests for Challenge 02: Quadratic Discriminant
========================================
Chapter 2: Your First Programs

Run with:
    python -m pytest code/python/ch02/tests/test_challenge_02.py -v
"""

import pytest

from ch02.practice.challenge_02_quadratic import solve


def test_two_real_roots():
    """x^2 - 3x + 2 = 0 has discriminant 1 and 2 real roots."""
    disc, num_roots = solve(1, -3, 2)
    assert disc == pytest.approx(1.0, abs=1e-4)
    assert num_roots == 2


def test_one_real_root():
    """x^2 + 2x + 1 = 0 has discriminant 0 and 1 real root (double root)."""
    disc, num_roots = solve(1, 2, 1)
    assert disc == pytest.approx(0.0, abs=1e-4)
    assert num_roots == 1


def test_no_real_roots():
    """x^2 + x + 1 = 0 has discriminant -3 and 0 real roots."""
    disc, num_roots = solve(1, 1, 1)
    assert disc == pytest.approx(-3.0, abs=1e-4)
    assert num_roots == 0


def test_large_discriminant():
    """x^2 - 10x + 1 = 0 has discriminant 96 and 2 real roots."""
    disc, num_roots = solve(1, -10, 1)
    assert disc == pytest.approx(96.0, abs=1e-4)
    assert num_roots == 2


def test_negative_coefficients():
    """2x^2 + 4x + 2 = 0 has discriminant 0 and 1 real root."""
    disc, num_roots = solve(2, 4, 2)
    assert disc == pytest.approx(0.0, abs=1e-4)
    assert num_roots == 1
