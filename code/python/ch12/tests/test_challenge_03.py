"""
Tests for Challenge 3: Minimum Bit Flips
==========================================
Chapter 12: Bit Manipulation — The Language of Computers

Run with:
    python -m pytest code/python/ch12/tests/test_challenge_03.py -v
"""
from ch12.practice.challenge_03_min_bit_flips import solve


def test_basic():
    assert solve(10, 7) == 3  # 1010 vs 0111


def test_three_four():
    assert solve(3, 4) == 3  # 011 vs 100


def test_same():
    assert solve(0, 0) == 0


def test_same_nonzero():
    assert solve(42, 42) == 0


def test_zero_to_max():
    assert solve(0, 255) == 8


def test_one_flip():
    assert solve(8, 0) == 1  # 1000 vs 0000


def test_large():
    assert solve(1023, 0) == 10  # 1111111111 vs 0
