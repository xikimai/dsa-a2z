"""
Tests for Warmup 2: Insert at Position
========================================
Chapter 21: Linked Lists — Pointers and Connections

Run with:
    python -m pytest code/python/ch21/tests/test_warmup_02.py -v
"""
from ch21.practice.warmup_02_insert_at_position import solve


def test_insert_middle():
    assert solve([1, 2, 3, 4], 10, 2) == [1, 2, 10, 3, 4]


def test_insert_at_head():
    assert solve([1, 2, 3], 0, 0) == [0, 1, 2, 3]


def test_insert_at_tail():
    assert solve([1, 2, 3], 4, 3) == [1, 2, 3, 4]


def test_insert_into_empty():
    assert solve([], 5, 0) == [5]


def test_insert_single():
    assert solve([1], 2, 1) == [1, 2]
