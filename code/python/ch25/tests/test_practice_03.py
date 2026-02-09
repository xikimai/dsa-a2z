"""
Tests for Practice 3: Edit Distance
======================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

Run with:
    python -m pytest code/python/ch25/tests/test_practice_03.py -v
"""
from ch25.practice.practice_03_edit_distance import solve


def test_basic():
    assert solve("horse", "ros") == 3


def test_longer():
    assert solve("intention", "execution") == 5


def test_empty_source():
    assert solve("", "abc") == 3


def test_identical():
    assert solve("abc", "abc") == 0


def test_empty_both():
    assert solve("", "") == 0


def test_single_replace():
    assert solve("a", "b") == 1
