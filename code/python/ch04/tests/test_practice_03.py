"""
Tests for Practice 3: Temperature Converter
========================================
Chapter 4: Functions

Run with:
    python -m pytest code/python/ch04/tests/test_practice_03.py -v
"""

from ch04.practice.practice_03_temperature import solve


def test_boiling_c_to_f():
    """100 C = 212 F."""
    assert solve(100.0, "C", "F") == 212.0


def test_freezing_f_to_c():
    """32 F = 0 C."""
    assert solve(32.0, "F", "C") == 0.0


def test_body_temp_c_to_f():
    """37 C = 98.6 F."""
    assert solve(37.0, "C", "F") == 98.6


def test_same_unit_c():
    """Same unit (C to C) returns value unchanged."""
    assert solve(100.0, "C", "C") == 100.0


def test_same_unit_f():
    """Same unit (F to F) returns value unchanged."""
    assert solve(72.0, "F", "F") == 72.0


def test_negative_temp():
    """Negative temperature conversion."""
    assert solve(-40.0, "C", "F") == -40.0


def test_invalid_from_unit():
    """Invalid from_unit returns -1.0."""
    assert solve(100.0, "K", "F") == -1.0


def test_invalid_to_unit():
    """Invalid to_unit returns -1.0."""
    assert solve(100.0, "C", "K") == -1.0
