"""
Tests for Challenge 3: Word Ladder
====================================
Chapter 19: Graphs I — Exploring Networks

Run with:
    python -m pytest code/python/ch19/tests/test_challenge_03.py -v
"""
from ch19.practice.challenge_03_word_ladder import solve


def test_basic():
    assert solve("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5


def test_no_path():
    assert solve("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0


def test_direct():
    assert solve("hot", "dot", ["dot"]) == 2


def test_single_letter():
    assert solve("a", "c", ["a", "b", "c"]) == 2


def test_end_not_in_list():
    assert solve("abc", "xyz", ["abd", "acd"]) == 0
