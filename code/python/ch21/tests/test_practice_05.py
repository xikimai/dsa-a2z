"""
Tests for Practice 5: Palindrome Linked List
==============================================
Chapter 21: Linked Lists — Pointers and Connections

Run with:
    python -m pytest code/python/ch21/tests/test_practice_05.py -v
"""
from ch21.practice.practice_05_palindrome import solve


def test_palindrome_odd():
    assert solve([1, 2, 3, 2, 1]) is True


def test_not_palindrome():
    assert solve([1, 2, 3, 4, 5]) is False


def test_single():
    assert solve([1]) is True


def test_empty():
    assert solve([]) is True


def test_palindrome_even():
    assert solve([1, 2, 2, 1]) is True


def test_two_same():
    assert solve([1, 1]) is True


def test_two_different():
    assert solve([1, 2]) is False
