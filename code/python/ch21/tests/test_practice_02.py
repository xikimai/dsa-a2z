"""
Tests for Practice 2: Detect Cycle
====================================
Chapter 21: Linked Lists — Pointers and Connections

Run with:
    python -m pytest code/python/ch21/tests/test_practice_02.py -v
"""
from ch21.practice.practice_02_detect_cycle import solve


def test_cycle_at_middle():
    assert solve([3, 2, 0, -4], 1) is True


def test_no_cycle():
    assert solve([1, 2], -1) is False


def test_self_loop():
    assert solve([1], 0) is True


def test_cycle_at_head():
    assert solve([1, 2, 3], 0) is True


def test_empty():
    assert solve([], -1) is False


def test_long_no_cycle():
    assert solve([1, 2, 3, 4, 5, 6, 7], -1) is False


def test_cycle_at_tail():
    assert solve([1, 2, 3, 4], 3) is True
