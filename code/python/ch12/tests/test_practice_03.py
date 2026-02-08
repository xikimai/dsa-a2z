"""
Tests for Practice 3: Set and Clear Bits
==========================================
Chapter 12: Bit Manipulation — The Language of Computers

Run with:
    python -m pytest code/python/ch12/tests/test_practice_03.py -v
"""
from ch12.practice.practice_03_set_and_clear_bits import solve_set, solve_clear


def test_set_unset_bit():
    assert solve_set(42, 0) == 43    # 101010 -> 101011


def test_set_already_set():
    assert solve_set(42, 1) == 42    # 101010 -> 101010


def test_set_from_zero():
    assert solve_set(0, 5) == 32


def test_clear_set_bit():
    assert solve_clear(42, 1) == 40  # 101010 -> 101000


def test_clear_already_clear():
    assert solve_clear(42, 0) == 42  # 101010 -> 101010


def test_clear_all_bits():
    n = 255  # 11111111
    for i in range(8):
        n = solve_clear(n, i)
    assert n == 0


def test_set_and_clear_roundtrip():
    n = 42
    n = solve_set(n, 0)   # set bit 0
    assert n == 43
    n = solve_clear(n, 0) # clear bit 0
    assert n == 42
