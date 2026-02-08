"""
Tests for Warmup 1: Factorial
========================================
Chapter 10: The Magic of Recursion

Run with:
    python -m pytest code/python/ch10/tests/test_warmup_01.py -v
"""
from ch10.practice.warmup_01_factorial import solve


def test_zero():
    assert solve(0) == 1


def test_one():
    assert solve(1) == 1


def test_five():
    assert solve(5) == 120


def test_ten():
    assert solve(10) == 3628800


def test_three():
    assert solve(3) == 6
