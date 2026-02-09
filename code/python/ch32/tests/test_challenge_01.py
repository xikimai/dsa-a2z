"""
Tests for Challenge 1: Word Search II
=======================================
Chapter 32: String Algorithms — Beyond Brute Force

Run with:
    python -m pytest code/python/ch32/tests/test_challenge_01.py -v
"""
from ch32.practice.challenge_01_word_search_ii import solve


def test_basic():
    board = [["o", "a", "a", "n"],
             ["e", "t", "a", "e"],
             ["i", "h", "k", "r"],
             ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    result = solve(board, words)
    assert sorted(result) == ["eat", "oath"]


def test_no_match():
    board = [["a", "b"], ["c", "d"]]
    words = ["abcb"]
    assert solve(board, words) == []


def test_single_cell():
    board = [["a"]]
    words = ["a", "b"]
    assert solve(board, words) == ["a"]


def test_adjacent_only():
    board = [["a", "b"], ["c", "d"]]
    words = ["ab", "ac", "bd", "cd", "ad"]
    result = solve(board, words)
    # ab (right), ac (down), bd (down), cd (right) are valid
    # ad is not valid (diagonal)
    assert sorted(result) == ["ab", "ac", "bd", "cd"]
