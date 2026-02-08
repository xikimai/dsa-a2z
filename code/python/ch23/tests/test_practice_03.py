"""
Tests for Practice 3: Decode Ways
=====================================
Chapter 23: Dynamic Programming I — The Foundation

Run with:
    python -m pytest code/python/ch23/tests/test_practice_03.py -v
"""
from ch23.practice.practice_03_decode_ways import solve


def test_twelve():
    assert solve("12") == 2


def test_two_two_six():
    assert solve("226") == 3


def test_leading_zero():
    assert solve("06") == 0


def test_single_digit():
    assert solve("1") == 1


def test_ten():
    assert solve("10") == 1


def test_twenty_seven():
    assert solve("27") == 1


def test_longer():
    assert solve("1234") == 3
