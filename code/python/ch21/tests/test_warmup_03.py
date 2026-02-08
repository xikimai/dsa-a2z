"""
Tests for Warmup 3: Delete Node at Position
=============================================
Chapter 21: Linked Lists — Pointers and Connections

Run with:
    python -m pytest code/python/ch21/tests/test_warmup_03.py -v
"""
from ch21.practice.warmup_03_delete_at_position import solve


def test_delete_middle():
    assert solve([1, 2, 3, 4, 5], 2) == [1, 2, 4, 5]


def test_delete_head():
    assert solve([1, 2, 3], 0) == [2, 3]


def test_delete_tail():
    assert solve([1, 2, 3], 2) == [1, 2]


def test_delete_single():
    assert solve([1], 0) == []


def test_delete_second():
    assert solve([10, 20, 30, 40], 1) == [10, 30, 40]
