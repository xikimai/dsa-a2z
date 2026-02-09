"""
Tests for Practice 5: Swim in Rising Water
============================================
Chapter 27: Shortest Paths — Finding the Best Route

Run with:
    python -m pytest code/python/ch27/tests/test_practice_05.py -v
"""
from ch27.practice.practice_05_swim_rising import solve


def test_2x2():
    assert solve([[0,2],[1,3]]) == 3


def test_5x5():
    grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],
            [11,17,18,19,20],[10,9,8,7,6]]
    assert solve(grid) == 16


def test_1x1():
    assert solve([[0]]) == 0


def test_sorted():
    assert solve([[0,1],[2,3]]) == 3
