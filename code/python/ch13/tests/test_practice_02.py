"""
Tests for Practice 2: N-Queens Count
Run with: python -m pytest code/python/ch13/tests/test_practice_02.py -v
"""
from ch13.practice.practice_02_n_queens_count import solve


def test_n1():
    assert solve(1) == 1


def test_n2():
    assert solve(2) == 0


def test_n3():
    assert solve(3) == 0


def test_n4():
    assert solve(4) == 2


def test_n5():
    assert solve(5) == 10


def test_n6():
    assert solve(6) == 4


def test_n8():
    assert solve(8) == 92
