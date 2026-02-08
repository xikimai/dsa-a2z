"""
Tests for Practice 1: Koko Eating Bananas
==========================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

Run with:
    python -m pytest code/python/ch16/tests/test_practice_01.py -v
"""
from ch16.practice.practice_01_koko_bananas import solve


def test_basic():
    assert solve([3, 6, 7, 11], 8) == 4


def test_single_pile():
    assert solve([30], 3) == 10


def test_equal_piles():
    assert solve([5, 5, 5, 5], 4) == 5


def test_generous_time():
    assert solve([3, 6, 7, 11], 20) == 2


def test_tight_time():
    assert solve([30, 11, 23, 4, 20], 5) == 30


def test_exact_fit():
    assert solve([10, 10, 10], 3) == 10


def test_one_pile_one_hour():
    assert solve([7], 1) == 7
