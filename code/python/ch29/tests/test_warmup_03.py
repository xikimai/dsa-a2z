"""
Tests for Warmup 3: Kruskal's MST
===================================
Chapter 29: Union-Find & Minimum Spanning Trees

Run with:
    python -m pytest code/python/ch29/tests/test_warmup_03.py -v
"""
from ch29.practice.warmup_03_kruskal_mst import solve


def test_basic():
    assert solve(4, [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]) == 19


def test_triangle():
    assert solve(3, [[0, 1, 1], [1, 2, 2], [0, 2, 3]]) == 3


def test_single_node():
    assert solve(1, []) == 0
