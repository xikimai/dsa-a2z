"""
Tests for Warmup 1: Binary Representation
===========================================
Chapter 12: Bit Manipulation — The Language of Computers

Run with:
    python -m pytest code/python/ch12/tests/test_warmup_01.py -v
"""
from ch12.practice.warmup_01_binary_representation import solve


def test_zero():
    assert solve(0) == "0"


def test_one():
    assert solve(1) == "1"


def test_small():
    assert solve(5) == "101"


def test_42():
    assert solve(42) == "101010"


def test_255():
    assert solve(255) == "11111111"


def test_1024():
    assert solve(1024) == "10000000000"


def test_large():
    assert solve(1000000000) == bin(1000000000)[2:]
