"""
Tests for Challenge 4: Palindrome Partitioning II
===================================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

Run with:
    python -m pytest code/python/ch31/tests/test_challenge_04.py -v
"""
from ch31.practice.challenge_04_palindrome_partition import solve


def test_aab():
    assert solve("aab") == 1


def test_single():
    assert solve("a") == 0


def test_ab():
    assert solve("ab") == 1


def test_aabb():
    assert solve("aabb") == 1


def test_palindrome():
    assert solve("aba") == 0
