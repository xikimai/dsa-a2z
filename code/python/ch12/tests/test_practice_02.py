"""
Tests for Practice 2: Toggle i-th Bit
=======================================
Chapter 12: Bit Manipulation — The Language of Computers

Run with:
    python -m pytest code/python/ch12/tests/test_practice_02.py -v
"""
from ch12.practice.practice_02_toggle_ith_bit import solve


def test_toggle_unset_bit():
    assert solve(42, 0) == 43  # 101010 -> 101011


def test_toggle_set_bit():
    assert solve(42, 1) == 40  # 101010 -> 101000


def test_toggle_from_zero():
    assert solve(0, 3) == 8  # 0000 -> 1000


def test_toggle_bit_5():
    assert solve(42, 5) == 10  # 101010 -> 001010


def test_toggle_twice():
    # Toggling twice returns to original
    assert solve(solve(42, 3), 3) == 42


def test_all_ones():
    assert solve(255, 0) == 254  # 11111111 -> 11111110
