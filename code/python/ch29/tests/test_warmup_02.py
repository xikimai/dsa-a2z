"""
Tests for Warmup 2: Redundant Connection
==========================================
Chapter 29: Union-Find & Minimum Spanning Trees

Run with:
    python -m pytest code/python/ch29/tests/test_warmup_02.py -v
"""
from ch29.practice.warmup_02_redundant_connection import solve


def test_triangle():
    assert solve([[1, 2], [1, 3], [2, 3]]) == [2, 3]


def test_longer():
    assert solve([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
