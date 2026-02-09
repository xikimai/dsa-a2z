"""
Tests for Challenge 2: Find Eventual Safe States
==================================================
Chapter 28: Topological Sort — Ordering Dependencies

Run with:
    python -m pytest code/python/ch28/tests/test_challenge_02.py -v
"""
from ch28.practice.challenge_02_eventual_safe_states import solve


def test_basic():
    assert solve([[1, 2], [2, 3], [5], [0], [5], [], []]) == [2, 4, 5, 6]


def test_cycle_heavy():
    assert solve([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]) == [4]


def test_all_safe():
    assert solve([[1], [2], []]) == [0, 1, 2]


def test_all_terminal():
    assert solve([[], [], []]) == [0, 1, 2]
