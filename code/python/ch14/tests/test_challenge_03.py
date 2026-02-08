"""
Tests for Challenge 3: Subarray Sum Divisible by K
=====================================================
Chapter 14: Prefix Sums — The Running Total Trick

Run with:
    python -m pytest code/python/ch14/tests/test_challenge_03.py -v
"""
from ch14.practice.challenge_03_subarray_divisible_k import solve


def test_basic():
    assert solve([4, 5, 0, -2, -3, 1], 5) == 7


def test_no_match():
    assert solve([5], 9) == 0


def test_all_divisible():
    assert solve([5, 10, 15], 5) == 6


def test_negative_elements():
    assert solve([-1, 2, 9], 2) == 2


def test_single_zero():
    assert solve([0], 1) == 1


def test_k_equals_1():
    # Every subarray sum is divisible by 1
    assert solve([1, 2, 3], 1) == 6
