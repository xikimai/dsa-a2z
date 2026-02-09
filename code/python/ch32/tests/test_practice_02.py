"""
Tests for Practice 2: Longest Common Prefix (Trie-based)
=========================================================
Chapter 32: String Algorithms — Beyond Brute Force

Run with:
    python -m pytest code/python/ch32/tests/test_practice_02.py -v
"""
from ch32.practice.practice_02_longest_common_prefix import solve


def test_partial_prefix():
    assert solve(["flower", "flow", "flight"]) == "fl"


def test_no_common():
    assert solve(["dog", "racecar", "car"]) == ""


def test_longer_prefix():
    assert solve(["interstellar", "internet", "internal"]) == "inter"


def test_single_word():
    assert solve(["a"]) == "a"


def test_identical():
    assert solve(["abc", "abc", "abc"]) == "abc"


def test_empty_string_in_list():
    assert solve(["", "abc"]) == ""
