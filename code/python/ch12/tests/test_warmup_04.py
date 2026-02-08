"""
Tests for Warmup 4: Check if i-th Bit Is Set
===============================================
Chapter 12: Bit Manipulation — The Language of Computers

Run with:
    python -m pytest code/python/ch12/tests/test_warmup_04.py -v
"""
from ch12.practice.warmup_04_check_ith_bit import solve


def test_42_bit_1():
    assert solve(42, 1) is True   # 101010


def test_42_bit_2():
    assert solve(42, 2) is False  # 101010


def test_42_bit_3():
    assert solve(42, 3) is True   # 101010


def test_42_bit_5():
    assert solve(42, 5) is True   # 101010


def test_42_bit_6():
    assert solve(42, 6) is False  # 101010


def test_zero():
    assert solve(0, 0) is False


def test_one_bit_0():
    assert solve(1, 0) is True


def test_power_of_two():
    assert solve(16, 4) is True
    assert solve(16, 3) is False
