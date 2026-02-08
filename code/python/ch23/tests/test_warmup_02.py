"""
Tests for Warmup 2: Fibonacci Number
========================================
Chapter 23: Dynamic Programming I — The Foundation

Run with:
    python -m pytest code/python/ch23/tests/test_warmup_02.py -v
"""
from ch23.practice.warmup_02_fibonacci import solve


def test_zero():
    assert solve(0) == 0


def test_one():
    assert solve(1) == 1


def test_two():
    assert solve(2) == 1


def test_ten():
    assert solve(10) == 55


def test_twenty():
    assert solve(20) == 6765
