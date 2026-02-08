"""
Tests for Challenge 4: Swim in Rising Water
========================================
Chapter 20: Graphs II — Real Problems

Run with:
    python -m pytest code/python/ch20/tests/test_challenge_04.py -v
"""
from ch20.practice.challenge_04_swim_in_rising_water import solve


def test_2x2():
    assert solve([[0, 2], [1, 3]]) == 3


def test_5x5():
    grid = [[0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6]]
    assert solve(grid) == 16


def test_1x1():
    assert solve([[0]]) == 0


def test_straight_path():
    grid = [[0, 1], [2, 3]]
    assert solve(grid) == 3


def test_avoid_high():
    grid = [[0, 1, 2],
            [5, 4, 3],
            [6, 7, 8]]
    assert solve(grid) == 8
