"""
Tests for Challenge 2: Two Numbers Appearing Odd Times
========================================================
Chapter 12: Bit Manipulation — The Language of Computers

Run with:
    python -m pytest code/python/ch12/tests/test_challenge_02.py -v
"""
from ch12.practice.challenge_02_two_odd_occurring import solve


def test_basic():
    assert solve([2, 4, 7, 9, 2, 4]) == [7, 9]


def test_three_four():
    assert solve([1, 2, 3, 2, 1, 4]) == [3, 4]


def test_just_two():
    assert solve([5, 10]) == [5, 10]


def test_many_pairs():
    assert solve([1, 1, 2, 2, 3, 3, 100, 200]) == [100, 200]


def test_odd_occurrences():
    # 7 appears 3 times (odd), 9 appears 1 time (odd), rest even
    assert solve([7, 7, 7, 9, 3, 3]) == [7, 9]


def test_large_numbers():
    assert solve([999999, 888888, 999999, 777777, 888888, 777777, 11, 22]) == [11, 22]
