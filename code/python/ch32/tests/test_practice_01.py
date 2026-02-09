"""
Tests for Practice 1: Rabin-Karp Pattern Search
=================================================
Chapter 32: String Algorithms — Beyond Brute Force

Run with:
    python -m pytest code/python/ch32/tests/test_practice_01.py -v
"""
from ch32.practice.practice_01_rabin_karp import solve


def test_multiple_matches():
    assert solve("AABAACAADAABAABA", "AABA") == [0, 9, 12]


def test_overlapping():
    assert solve("ABABABAB", "ABAB") == [0, 2, 4]


def test_full_match():
    assert solve("HELLO", "HELLO") == [0]


def test_no_match():
    assert solve("HELLO", "WORLD") == []


def test_single_char():
    assert solve("AAAA", "A") == [0, 1, 2, 3]
