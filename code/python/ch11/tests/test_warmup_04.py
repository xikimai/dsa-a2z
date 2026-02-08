"""
Tests for Warmup 4: Valid Anagram
========================================
Chapter 11: Hashing — The Secret Decoder Ring

Run with:
    python -m pytest code/python/ch11/tests/test_warmup_04.py -v
"""
from ch11.practice.warmup_04_valid_anagram import solve


def test_anagram():
    assert solve("listen", "silent") == True


def test_not_anagram():
    assert solve("hello", "world") == False


def test_empty():
    assert solve("", "") == True


def test_single():
    assert solve("a", "a") == True


def test_swap():
    assert solve("ab", "ba") == True


def test_diff_char():
    assert solve("abc", "abd") == False


def test_rearranged():
    assert solve("aab", "aba") == True
