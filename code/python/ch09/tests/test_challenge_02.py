"""
Tests for Challenge 2: Single Element in Sorted Array
========================================
Chapter 9: Finding Needles — The Power of Searching

Run with:
    python -m pytest code/python/ch09/tests/test_challenge_02.py -v
"""
from ch09.practice.challenge_02_single_element import solve


def test_single_in_middle():
    assert solve([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2


def test_single_in_middle_2():
    assert solve([3, 3, 7, 7, 10, 11, 11]) == 10


def test_single_element_only():
    assert solve([1]) == 1


def test_single_at_end():
    assert solve([1, 1, 2]) == 2


def test_single_at_start():
    assert solve([1, 2, 2]) == 1
