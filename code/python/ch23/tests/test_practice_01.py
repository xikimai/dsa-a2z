"""
Tests for Practice 1: Frog Jump with K Steps
================================================
Chapter 23: Dynamic Programming I — The Foundation

Run with:
    python -m pytest code/python/ch23/tests/test_practice_01.py -v
"""
from ch23.practice.practice_01_frog_jump_k import solve


def test_basic_k2():
    assert solve([0, 3, 2, 6, 1], 2) == 3


def test_k3():
    assert solve([10, 20, 30, 10], 3) == 20


def test_single():
    assert solve([5], 1) == 5


def test_k1():
    assert solve([10, 30, 40, 20], 1) == 100


def test_k2():
    assert solve([10, 30, 40, 20], 2) == 60


def test_larger():
    assert solve([1, 3, 5, 2, 1, 4], 3) == 7
