"""
Tests for Challenge 2: Trapping Rain Water
============================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

Run with:
    python -m pytest code/python/ch15/tests/test_challenge_02.py -v
"""
from ch15.practice.challenge_02_trapping_rain_water import solve


def test_basic():
    assert solve([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_v_shape():
    assert solve([4, 2, 0, 3, 2, 5]) == 9


def test_flat():
    assert solve([3, 3, 3]) == 0


def test_ascending():
    assert solve([1, 2, 3, 4]) == 0


def test_descending():
    assert solve([4, 3, 2, 1]) == 0


def test_empty():
    assert solve([]) == 0


def test_two_elements():
    assert solve([1, 2]) == 0


def test_single():
    assert solve([5]) == 0
