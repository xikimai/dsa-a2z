"""
Tests for Challenge 1: Three Sum
==================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

Run with:
    python -m pytest code/python/ch15/tests/test_challenge_01.py -v
"""
from ch15.practice.challenge_01_three_sum import solve


def test_basic():
    assert solve([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]


def test_no_triplet():
    assert solve([0, 1, 1]) == []


def test_all_zeros():
    assert solve([0, 0, 0]) == [[0, 0, 0]]


def test_all_zeros_extra():
    assert solve([0, 0, 0, 0]) == [[0, 0, 0]]


def test_no_result():
    assert solve([1, 2, 3]) == []


def test_multiple_triplets():
    result = solve([-2, -1, 0, 1, 2, 3])
    assert [-2, -1, 3] in result
    assert [-2, 0, 2] in result
    assert [-1, 0, 1] in result
    assert len(result) == 3
