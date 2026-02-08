"""
Tests for Practice 5: Dutch National Flag
===========================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

Run with:
    python -m pytest code/python/ch15/tests/test_practice_05.py -v
"""
from ch15.practice.practice_05_dutch_national_flag import solve


def test_basic():
    assert solve([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]


def test_three_elements():
    assert solve([2, 0, 1]) == [0, 1, 2]


def test_already_sorted():
    assert solve([0, 0, 1, 1, 2, 2]) == [0, 0, 1, 1, 2, 2]


def test_reverse_sorted():
    assert solve([2, 2, 1, 1, 0, 0]) == [0, 0, 1, 1, 2, 2]


def test_all_same():
    assert solve([1, 1, 1]) == [1, 1, 1]


def test_single():
    assert solve([0]) == [0]


def test_empty():
    assert solve([]) == []


def test_only_zeros_and_twos():
    assert solve([2, 0, 2, 0]) == [0, 0, 2, 2]
