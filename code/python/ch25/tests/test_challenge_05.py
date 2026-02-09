"""
Tests for Challenge 5: Minimum Insertions for Palindrome
===========================================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

Run with:
    python -m pytest code/python/ch25/tests/test_challenge_05.py -v
"""
from ch25.practice.challenge_05_min_insertions_palindrome import solve


def test_already_palindrome():
    assert solve("zzazz") == 0


def test_basic():
    assert solve("mbadm") == 2


def test_longer():
    assert solve("leetcode") == 5


def test_single():
    assert solve("a") == 0


def test_two_same():
    assert solve("aa") == 0


def test_two_diff():
    assert solve("ab") == 1
