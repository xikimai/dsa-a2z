"""
Tests for Warmup 5: Power
========================================
Chapter 10: The Magic of Recursion

Run with:
    python -m pytest code/python/ch10/tests/test_warmup_05.py -v
"""
from ch10.practice.warmup_05_power import solve


def test_anything_to_zero():
    assert solve(2, 0) == 1


def test_two_to_ten():
    assert solve(2, 10) == 1024


def test_three_to_four():
    assert solve(3, 4) == 81


def test_five_to_three():
    assert solve(5, 3) == 125


def test_one_to_hundred():
    assert solve(1, 100) == 1
