"""
Tests for Warmup 4: Shortest Path in Binary Matrix
====================================================
Chapter 27: Shortest Paths — Finding the Best Route

Run with:
    python -m pytest code/python/ch27/tests/test_warmup_04.py -v
"""
from ch27.practice.warmup_04_binary_matrix import solve


def test_2x2():
    assert solve([[0,1],[1,0]]) == 2


def test_3x3():
    assert solve([[0,0,0],[1,1,0],[1,1,0]]) == 4


def test_blocked_start():
    assert solve([[1,0,0],[0,0,0],[0,0,0]]) == -1


def test_single_cell():
    assert solve([[0]]) == 1


def test_blocked_end():
    assert solve([[0,0],[0,1]]) == -1
