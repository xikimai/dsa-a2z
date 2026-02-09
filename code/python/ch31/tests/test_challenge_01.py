"""
Tests for Challenge 1: Minimum Cost to Merge Stones
=====================================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

Run with:
    python -m pytest code/python/ch31/tests/test_challenge_01.py -v
"""
from ch31.practice.challenge_01_merge_stones import solve


def test_k2():
    assert solve([3, 2, 4, 1], 2) == 20


def test_k3():
    assert solve([3, 5, 1, 2, 6], 3) == 25


def test_impossible():
    assert solve([3, 2, 4, 1], 3) == -1


def test_single():
    assert solve([5], 2) == 0
