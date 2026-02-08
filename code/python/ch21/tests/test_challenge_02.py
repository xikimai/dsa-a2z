"""
Tests for Challenge 2: Intersection of Two Lists
==================================================
Chapter 21: Linked Lists — Pointers and Connections

Run with:
    python -m pytest code/python/ch21/tests/test_challenge_02.py -v
"""
from ch21.practice.challenge_02_intersection import solve


def test_basic_intersection():
    assert solve([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3) == 8


def test_no_intersection():
    assert solve([1, 2, 3], [4, 5, 6], 3, 3) == -1


def test_intersection_at_head():
    assert solve([1, 2, 3], [1, 2, 3], 0, 0) == 1


def test_different_prefix_lengths():
    assert solve([1, 9, 1, 2, 4], [3, 2, 4], 3, 1) == 2


def test_single_shared_node():
    assert solve([1, 2, 7], [3, 4, 5, 7], 2, 3) == 7
