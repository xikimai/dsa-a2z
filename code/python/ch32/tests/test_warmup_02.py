"""
Tests for Warmup 2: Trie Prefix Count
=======================================
Chapter 32: String Algorithms — Beyond Brute Force

Run with:
    python -m pytest code/python/ch32/tests/test_warmup_02.py -v
"""
from ch32.practice.warmup_02_trie_prefix_count import solve


def test_basic():
    assert solve(["apple", "app", "application", "apt", "banana"],
                 ["app", "a", "ban", "c"]) == [3, 4, 1, 0]


def test_all_same_prefix():
    assert solve(["test", "testing", "tested"],
                 ["test", "tes"]) == [3, 3]


def test_no_match():
    assert solve(["abc", "abd"], ["xyz"]) == [0]


def test_single_char():
    assert solve(["a", "ab", "abc"], ["a", "ab", "abc", "abcd"]) == [3, 2, 1, 0]


def test_empty_prefix_list():
    assert solve(["hello"], []) == []
