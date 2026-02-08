"""
Tests for Practice 1: Single Number
=====================================
Chapter 12: Bit Manipulation — The Language of Computers

Run with:
    python -m pytest code/python/ch12/tests/test_practice_01.py -v
"""
from ch12.practice.practice_01_single_number import solve


def test_basic():
    assert solve([4, 1, 2, 1, 2]) == 4


def test_small():
    assert solve([2, 2, 1]) == 1


def test_single():
    assert solve([1]) == 1


def test_larger():
    assert solve([1, 3, 5, 3, 1]) == 5


def test_negative():
    assert solve([-1, 2, -1]) == 2


def test_zero():
    assert solve([0, 5, 0]) == 5
