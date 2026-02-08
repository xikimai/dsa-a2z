"""
Tests for Challenge 2: Gas Station
=====================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

Run with:
    python -m pytest code/python/ch18/tests/test_challenge_02.py -v
"""
from ch18.practice.challenge_02_gas_station import solve


def test_basic():
    assert solve([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3


def test_impossible():
    assert solve([2, 3, 4], [3, 4, 3]) == -1


def test_start_at_last():
    assert solve([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]) == 4


def test_single_station():
    assert solve([5], [4]) == 0


def test_single_impossible():
    assert solve([3], [5]) == -1


def test_start_at_zero():
    assert solve([3, 1, 1], [1, 2, 2]) == 0


def test_all_equal():
    assert solve([3, 3, 3], [3, 3, 3]) == 0
