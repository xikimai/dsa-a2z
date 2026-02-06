"""
Tests for Warmup 03: Celsius to Fahrenheit
========================================
Chapter 2: Your First Programs

Run with:
    python -m pytest code/python/ch02/tests/test_warmup_03.py -v
"""

import pytest

from ch02.practice.warmup_03_celsius_to_fahrenheit import solve


def test_freezing_point():
    """0 degrees Celsius is 32 degrees Fahrenheit."""
    assert solve(0.0) == pytest.approx(32.0, abs=1e-4)


def test_boiling_point():
    """100 degrees Celsius is 212 degrees Fahrenheit."""
    assert solve(100.0) == pytest.approx(212.0, abs=1e-4)


def test_negative_forty():
    """-40 is the same in both Celsius and Fahrenheit."""
    assert solve(-40.0) == pytest.approx(-40.0, abs=1e-4)


def test_body_temperature():
    """37 degrees Celsius is 98.6 degrees Fahrenheit."""
    assert solve(37.0) == pytest.approx(98.6, abs=1e-4)


def test_room_temperature():
    """20 degrees Celsius is 68 degrees Fahrenheit."""
    assert solve(20.0) == pytest.approx(68.0, abs=1e-4)
