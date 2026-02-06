"""
Tests for Challenge 2: Group Anagrams
=======================================
Chapter 5: Collections

Run with:
    python -m pytest code/python/ch05/tests/test_challenge_02.py -v
"""

from ch05.practice.challenge_02_group_anagrams import solve


def test_basic_case():
    """Classic anagram grouping example."""
    result = solve(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert result == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]


def test_single_empty_string():
    """Single empty string forms its own group."""
    assert solve([""]) == [[""]]


def test_single_string():
    """Single non-empty string forms its own group."""
    assert solve(["a"]) == [["a"]]


def test_no_anagrams():
    """No strings are anagrams of each other."""
    result = solve(["abc", "def", "ghi"])
    assert result == [["abc"], ["def"], ["ghi"]]


def test_all_anagrams():
    """All strings are anagrams of each other."""
    result = solve(["abc", "bca", "cab"])
    assert result == [["abc", "bca", "cab"]]
