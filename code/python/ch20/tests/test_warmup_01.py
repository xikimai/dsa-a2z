"""
Tests for Warmup 1: Flood Fill
========================================
Chapter 20: Graphs II — Real Problems

Run with:
    python -m pytest code/python/ch20/tests/test_warmup_01.py -v
"""
from ch20.practice.warmup_01_flood_fill import solve


def test_basic():
    assert solve([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]


def test_same_color():
    assert solve([[0, 0, 0], [0, 0, 0]], 0, 0, 0) == [[0, 0, 0], [0, 0, 0]]


def test_single_cell():
    assert solve([[5]], 0, 0, 3) == [[3]]


def test_corner():
    assert solve([[1, 2], [3, 4]], 0, 0, 9) == [[9, 2], [3, 4]]


def test_large_connected():
    assert solve([[1, 1], [1, 1]], 0, 0, 7) == [[7, 7], [7, 7]]


def test_disconnected_region():
    assert solve([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 1, 1, 5) == [[0, 0, 0], [0, 5, 0], [0, 0, 0]]
