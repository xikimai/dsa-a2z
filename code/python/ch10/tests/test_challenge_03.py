"""
Tests for Challenge 3: Combination Sum
========================================
Chapter 10: The Magic of Recursion

Run with:
    python -m pytest code/python/ch10/tests/test_challenge_03.py -v
"""
from ch10.practice.challenge_03_combination_sum import solve


def test_example_one():
    assert solve([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]


def test_example_two():
    assert solve([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]


def test_no_solution():
    assert solve([2], 1) == []


def test_single_match():
    assert solve([1], 1) == [[1]]


def test_repeated_ones():
    assert solve([1], 3) == [[1, 1, 1]]
