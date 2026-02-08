"""
Tests for Warmup 3: Reverse String
========================================
Chapter 10: The Magic of Recursion

Run with:
    python -m pytest code/python/ch10/tests/test_warmup_03.py -v
"""
from ch10.practice.warmup_03_reverse_string import solve


def test_hello():
    assert solve("hello") == "olleh"


def test_single_char():
    assert solve("a") == "a"


def test_empty():
    assert solve("") == ""


def test_two_chars():
    assert solve("ab") == "ba"


def test_five_chars():
    assert solve("abcde") == "edcba"
