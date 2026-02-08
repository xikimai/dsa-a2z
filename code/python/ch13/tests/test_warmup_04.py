"""
Tests for Warmup 4: Count Binary Strings
Run with: python -m pytest code/python/ch13/tests/test_warmup_04.py -v
"""
from ch13.practice.warmup_04_count_binary_strings import solve


def test_n1():
    assert solve(1) == 2


def test_n2():
    assert solve(2) == 3


def test_n3():
    assert solve(3) == 5


def test_n4():
    assert solve(4) == 8


def test_n5():
    assert solve(5) == 13


def test_n10():
    assert solve(10) == 144


def test_n20():
    assert solve(20) == 17711
