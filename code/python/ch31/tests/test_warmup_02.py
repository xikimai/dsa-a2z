"""
Tests for Warmup 2: Matrix Chain Multiplication
=================================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

Run with:
    python -m pytest code/python/ch31/tests/test_warmup_02.py -v
"""
from ch31.practice.warmup_02_mcm import solve


def test_three_matrices():
    assert solve([10, 30, 5, 60]) == 4500


def test_four_matrices():
    assert solve([40, 20, 30, 10, 30]) == 26000


def test_two_matrices():
    assert solve([10, 20, 30]) == 6000


def test_single_matrix():
    assert solve([5, 10]) == 0


def test_five_matrices():
    # A(10x20) B(20x30) C(30x40) D(40x30)
    assert solve([10, 20, 30, 40, 30]) == 30000
