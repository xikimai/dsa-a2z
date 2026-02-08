"""
Tests for Practice 1: Fibonacci
========================================
Chapter 10: The Magic of Recursion

Run with:
    python -m pytest code/python/ch10/tests/test_practice_01.py -v
"""
from ch10.practice.practice_01_fibonacci import solve


def test_fib_zero():
    assert solve(0) == 0


def test_fib_one():
    assert solve(1) == 1


def test_fib_five():
    assert solve(5) == 5


def test_fib_ten():
    assert solve(10) == 55


def test_fib_fifteen():
    assert solve(15) == 610
