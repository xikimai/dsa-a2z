"""
Tests for Practice 4: Repeated String Match
=============================================
Chapter 32: String Algorithms — Beyond Brute Force

Run with:
    python -m pytest code/python/ch32/tests/test_practice_04.py -v
"""
from ch32.practice.practice_04_repeated_string_match import solve


def test_three_repeats():
    assert solve("abcd", "cdabcdab") == 3


def test_two_repeats():
    assert solve("a", "aa") == 2


def test_impossible():
    assert solve("abc", "xyz") == -1


def test_one_repeat():
    assert solve("abc", "abc") == 1


def test_single_char():
    assert solve("a", "a") == 1
