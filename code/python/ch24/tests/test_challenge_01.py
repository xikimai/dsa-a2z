"""
Tests for Challenge 1: Dungeon Game
======================================
Chapter 24: Dynamic Programming II — Grids and Paths

Run with:
    python -m pytest code/python/ch24/tests/test_challenge_01.py -v
"""
from ch24.practice.challenge_01_dungeon import solve


def test_basic():
    assert solve([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]) == 7


def test_zero():
    assert solve([[0]]) == 1


def test_positive():
    assert solve([[100]]) == 1


def test_negative_only():
    assert solve([[-5]]) == 6


def test_single_row():
    assert solve([[-2, -3, 3]]) == 6
