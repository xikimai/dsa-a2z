"""
Tests for Practice 2: Missing Number
========================================
Chapter 11: Hashing — The Secret Decoder Ring

Run with:
    python -m pytest code/python/ch11/tests/test_practice_02.py -v
"""
from ch11.practice.practice_02_missing_number import solve


def test_basic():
    assert solve([3, 0, 1]) == 2


def test_last():
    assert solve([0, 1]) == 2


def test_large():
    assert solve([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


def test_missing_last():
    assert solve([0]) == 1


def test_missing_first():
    assert solve([1]) == 0
