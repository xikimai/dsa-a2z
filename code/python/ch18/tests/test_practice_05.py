"""
Tests for Practice 5: Jump Game II
=====================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

Run with:
    python -m pytest code/python/ch18/tests/test_practice_05.py -v
"""
from ch18.practice.practice_05_jump_game_ii import solve


def test_basic():
    assert solve([2, 3, 1, 1, 4]) == 2


def test_with_zeros():
    assert solve([2, 3, 0, 1, 4]) == 2


def test_single():
    assert solve([1]) == 0


def test_two():
    assert solve([1, 1]) == 1


def test_big_jump():
    assert solve([10, 0, 0, 0, 0]) == 1


def test_all_ones():
    assert solve([1, 1, 1, 1, 1]) == 4


def test_decreasing():
    assert solve([4, 3, 2, 1, 0]) == 1
