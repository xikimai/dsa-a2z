"""
Tests for Practice 3: Product of Array Except Self
=====================================================
Chapter 14: Prefix Sums — The Running Total Trick

Run with:
    python -m pytest code/python/ch14/tests/test_practice_03.py -v
"""
from ch14.practice.practice_03_product_except_self import solve


def test_basic():
    assert solve([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_with_zero():
    assert solve([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_two_elements():
    assert solve([3, 5]) == [5, 3]


def test_with_negatives():
    assert solve([-1, -2, -3]) == [6, 3, 2]


def test_with_ones():
    assert solve([1, 1, 1, 1]) == [1, 1, 1, 1]


def test_two_zeros():
    assert solve([0, 0, 1]) == [0, 0, 0]
