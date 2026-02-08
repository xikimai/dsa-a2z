"""
Tests for Warmup 2: Count Set Bits
====================================
Chapter 12: Bit Manipulation — The Language of Computers

Run with:
    python -m pytest code/python/ch12/tests/test_warmup_02.py -v
"""
from ch12.practice.warmup_02_count_set_bits import solve


def test_zero():
    assert solve(0) == 0


def test_one():
    assert solve(1) == 1


def test_42():
    assert solve(42) == 3  # 101010


def test_255():
    assert solve(255) == 8  # 11111111


def test_1023():
    assert solve(1023) == 10  # 1111111111


def test_power_of_two():
    assert solve(1024) == 1  # 10000000000


def test_large():
    assert solve(999999999) == bin(999999999).count('1')
