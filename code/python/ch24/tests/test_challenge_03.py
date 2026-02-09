"""
Tests for Challenge 3: Ninja Training
========================================
Chapter 24: Dynamic Programming II — Grids and Paths

Run with:
    python -m pytest code/python/ch24/tests/test_challenge_03.py -v
"""
from ch24.practice.challenge_03_ninja_training import solve


def test_basic():
    assert solve([[10, 40, 70], [20, 50, 80], [30, 60, 90]]) == 210


def test_small():
    assert solve([[1, 2, 5], [3, 1, 1], [3, 3, 3]]) == 11


def test_single_day():
    assert solve([[10, 10, 10]]) == 10


def test_two_days():
    assert solve([[1, 2, 3], [3, 2, 1]]) == 6


def test_uniform():
    assert solve([[5, 5, 5], [5, 5, 5], [5, 5, 5]]) == 15
