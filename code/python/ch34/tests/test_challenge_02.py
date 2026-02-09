"""
Tests for Challenge 2: Maximum Rectangle in Histogram
=======================================================
Chapter 34: Computational Geometry & Sweep Line

Run with:
    python -m pytest code/python/ch34/tests/test_challenge_02.py -v
"""
from ch34.practice.challenge_02_max_rectangle_histogram import solve


def test_basic():
    assert solve([2, 1, 5, 6, 2, 3]) == 10


def test_two_bars():
    assert solve([2, 4]) == 4


def test_single_bar():
    assert solve([1]) == 1


def test_increasing():
    assert solve([1, 2, 3, 4, 5]) == 9  # 3*3


def test_decreasing():
    assert solve([5, 4, 3, 2, 1]) == 9  # 3*3


def test_all_same():
    assert solve([3, 3, 3, 3]) == 12  # 3*4
