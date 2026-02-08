"""
Tests for Practice 1: Container With Most Water
=================================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

Run with:
    python -m pytest code/python/ch15/tests/test_practice_01.py -v
"""
from ch15.practice.practice_01_container_most_water import solve


def test_basic():
    assert solve([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_two_elements():
    assert solve([1, 1]) == 1


def test_decreasing():
    assert solve([4, 3, 2, 1]) == 4


def test_increasing():
    assert solve([1, 2, 3, 4]) == 4


def test_equal_heights():
    assert solve([5, 5, 5, 5]) == 15


def test_tall_ends():
    assert solve([10, 1, 1, 1, 10]) == 40
