"""
Tests for Challenge 1: Find Cycle Start
=========================================
Chapter 21: Linked Lists — Pointers and Connections

Run with:
    python -m pytest code/python/ch21/tests/test_challenge_01.py -v
"""
from ch21.practice.challenge_01_cycle_start import solve


def test_cycle_at_index_1():
    assert solve([3, 2, 0, -4], 1) == 1


def test_cycle_at_index_0():
    assert solve([1, 2], 0) == 0


def test_no_cycle():
    assert solve([1], -1) == -1


def test_self_loop():
    assert solve([1], 0) == 0


def test_cycle_at_index_2():
    assert solve([1, 2, 3, 4, 5], 2) == 2


def test_empty():
    assert solve([], -1) == -1
