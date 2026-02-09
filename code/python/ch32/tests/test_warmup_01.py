"""
Tests for Warmup 1: Trie Insert and Search
===========================================
Chapter 32: String Algorithms — Beyond Brute Force

Run with:
    python -m pytest code/python/ch32/tests/test_warmup_01.py -v
"""
from ch32.practice.warmup_01_trie_search import solve


def test_basic():
    assert solve(["apple", "app", "banana"],
                 ["app", "apple", "ban", "banana"]) == [True, True, False, True]


def test_single_word():
    assert solve(["hello"],
                 ["hello", "hell", "helloo"]) == [True, False, False]


def test_empty_queries():
    assert solve(["a", "b"], []) == []


def test_no_match():
    assert solve(["cat", "dog"], ["bird", "fish"]) == [False, False]


def test_prefix_not_word():
    assert solve(["application"], ["app", "application"]) == [False, True]
