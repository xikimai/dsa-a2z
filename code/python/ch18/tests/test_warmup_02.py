"""
Tests for Warmup 2: Jump Game I
==================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

Run with:
    python -m pytest code/python/ch18/tests/test_warmup_02.py -v
"""
from ch18.practice.warmup_02_jump_game import solve


def test_reachable():
    assert solve([2, 3, 1, 1, 4]) is True


def test_unreachable():
    assert solve([3, 2, 1, 0, 4]) is False


def test_single():
    assert solve([0]) is True


def test_two_reachable():
    assert solve([1, 0]) is True


def test_two_unreachable():
    assert solve([0, 1]) is False


def test_all_ones():
    assert solve([1, 1, 1, 1]) is True


def test_big_first_jump():
    assert solve([5, 0, 0, 0, 0, 0]) is True


def test_zeros_in_middle():
    assert solve([2, 0, 0]) is True
