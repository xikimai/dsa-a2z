"""
Tests for Challenge 2: Shortest Palindrome
============================================
Chapter 32: String Algorithms — Beyond Brute Force

Run with:
    python -m pytest code/python/ch32/tests/test_challenge_02.py -v
"""
from ch32.practice.challenge_02_shortest_palindrome import solve


def test_almost_palindrome():
    assert solve("aacecaaa") == "aaacecaaa"


def test_no_palindrome():
    assert solve("abcd") == "dcbabcd"


def test_single_char():
    assert solve("a") == "a"


def test_empty():
    assert solve("") == ""


def test_already_palindrome():
    assert solve("aba") == "aba"


def test_two_chars():
    assert solve("ab") == "bab"
