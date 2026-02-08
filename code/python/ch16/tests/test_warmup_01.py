"""
Tests for Warmup 1: Square Root (Integer)
==========================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

Run with:
    python -m pytest code/python/ch16/tests/test_warmup_01.py -v
"""
from ch16.practice.warmup_01_square_root import solve


def test_perfect_square():
    assert solve(16) == 4


def test_non_perfect():
    assert solve(8) == 2  # floor(sqrt(8)) = 2


def test_zero():
    assert solve(0) == 0


def test_one():
    assert solve(1) == 1


def test_large_perfect():
    assert solve(100) == 10


def test_large_non_perfect():
    assert solve(99) == 9


def test_small():
    assert solve(2) == 1


def test_49():
    assert solve(49) == 7
