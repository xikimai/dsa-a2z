"""
Tests for Practice 6: Tribonacci Number
==========================================
Chapter 23: Dynamic Programming I — The Foundation

Run with:
    python -m pytest code/python/ch23/tests/test_practice_06.py -v
"""
from ch23.practice.practice_06_tribonacci import solve


def test_zero():
    assert solve(0) == 0


def test_one():
    assert solve(1) == 1


def test_two():
    assert solve(2) == 1


def test_four():
    assert solve(4) == 4


def test_twenty_five():
    assert solve(25) == 1389537
