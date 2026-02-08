"""
Tests for Challenge 2: Painter's Partition
===========================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

Run with:
    python -m pytest code/python/ch16/tests/test_challenge_02.py -v
"""
from ch16.practice.challenge_02_painters_partition import solve


def test_basic():
    assert solve([10, 20, 30, 40], 2) == 60


def test_single_painter():
    assert solve([10, 20, 30], 1) == 60


def test_one_board_each():
    assert solve([10, 20, 30], 3) == 30


def test_equal_boards():
    assert solve([25, 25, 25, 25], 2) == 50


def test_more_painters_than_boards():
    assert solve([10, 20], 5) == 20


def test_large_board():
    assert solve([5, 5, 5, 100], 2) == 100


def test_many_painters():
    assert solve([1, 2, 3, 4, 5], 5) == 5
