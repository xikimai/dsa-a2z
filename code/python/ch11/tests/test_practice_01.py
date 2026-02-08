"""
Tests for Practice 1: Group Anagrams
========================================
Chapter 11: Hashing — The Secret Decoder Ring

Run with:
    python -m pytest code/python/ch11/tests/test_practice_01.py -v
"""
from ch11.practice.practice_01_group_anagrams import solve


def test_basic():
    assert solve(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["ate", "eat", "tea"],
        ["bat"],
        ["nat", "tan"],
    ]


def test_single_empty():
    assert solve([""]) == [[""]]


def test_single():
    assert solve(["a"]) == [["a"]]


def test_two_groups():
    assert solve(["abc", "bca", "cab", "xyz", "zxy"]) == [
        ["abc", "bca", "cab"],
        ["xyz", "zxy"],
    ]


def test_empty():
    assert solve([]) == []
