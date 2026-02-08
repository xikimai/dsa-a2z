"""
Tests for Practice 1: Find Middle Node
========================================
Chapter 21: Linked Lists — Pointers and Connections

Run with:
    python -m pytest code/python/ch21/tests/test_practice_01.py -v
"""
from ch21.practice.practice_01_find_middle import solve


def test_odd_length():
    assert solve([1, 2, 3, 4, 5]) == 3


def test_even_length():
    assert solve([1, 2, 3, 4]) == 3  # second middle


def test_single():
    assert solve([1]) == 1


def test_two_elements():
    assert solve([1, 2]) == 2  # second middle


def test_three_elements():
    assert solve([10, 20, 30]) == 20


def test_six_elements():
    assert solve([1, 2, 3, 4, 5, 6]) == 4  # second middle
