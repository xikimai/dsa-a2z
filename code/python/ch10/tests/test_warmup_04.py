"""
Tests for Warmup 4: Check Palindrome
========================================
Chapter 10: The Magic of Recursion

Run with:
    python -m pytest code/python/ch10/tests/test_warmup_04.py -v
"""
from ch10.practice.warmup_04_check_palindrome import solve


def test_racecar():
    assert solve("racecar") is True


def test_hello():
    assert solve("hello") is False


def test_empty():
    assert solve("") is True


def test_single_char():
    assert solve("a") is True


def test_two_different():
    assert solve("ab") is False


def test_three_palindrome():
    assert solve("aba") is True
