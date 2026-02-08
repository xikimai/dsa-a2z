"""
Tests for Warmup 2: Sum of First N
========================================
Chapter 10: The Magic of Recursion

Run with:
    python -m pytest code/python/ch10/tests/test_warmup_02.py -v
"""
from ch10.practice.warmup_02_sum_first_n import solve


def test_zero():
    assert solve(0) == 0


def test_one():
    assert solve(1) == 1


def test_five():
    assert solve(5) == 15


def test_ten():
    assert solve(10) == 55


def test_hundred():
    assert solve(100) == 5050
