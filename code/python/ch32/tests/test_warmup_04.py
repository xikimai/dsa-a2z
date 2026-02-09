"""
Tests for Warmup 4: Z-Function
================================
Chapter 32: String Algorithms — Beyond Brute Force

Run with:
    python -m pytest code/python/ch32/tests/test_warmup_04.py -v
"""
from ch32.practice.warmup_04_z_function import solve


def test_mixed():
    assert solve("aabxaa") == [0, 1, 0, 0, 2, 1]


def test_all_same():
    assert solve("aaaaa") == [0, 4, 3, 2, 1]


def test_all_different():
    assert solve("abcdef") == [0, 0, 0, 0, 0, 0]


def test_single_char():
    assert solve("a") == [0]


def test_two_chars_same():
    assert solve("aa") == [0, 1]


def test_two_chars_diff():
    assert solve("ab") == [0, 0]
