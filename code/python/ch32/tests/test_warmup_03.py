"""
Tests for Warmup 3: KMP Pattern Search
========================================
Chapter 32: String Algorithms — Beyond Brute Force

Run with:
    python -m pytest code/python/ch32/tests/test_warmup_03.py -v
"""
from ch32.practice.warmup_03_kmp_search import solve


def test_multiple_matches():
    assert solve("AABAACAADAABAABA", "AABA") == [0, 9, 12]


def test_two_matches():
    assert solve("ABCABC", "ABC") == [0, 3]


def test_overlapping():
    assert solve("AAAAA", "AA") == [0, 1, 2, 3]


def test_no_match():
    assert solve("HELLO", "WORLD") == []


def test_full_match():
    assert solve("ABC", "ABC") == [0]


def test_single_char_pattern():
    assert solve("ABABA", "A") == [0, 2, 4]
