"""
Tests for Challenge 03: Collatz Sequence
========================================
Chapter 3: Decisions and Loops

Run with:
    python -m pytest code/python/ch03/tests/test_challenge_03.py -v
"""

from ch03.practice.challenge_03_collatz import solve


def test_six():
    """Collatz sequence starting from 6."""
    assert solve(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]


def test_one():
    """Collatz sequence starting from 1 is just [1]."""
    assert solve(1) == [1]


def test_two():
    """Collatz sequence starting from 2."""
    assert solve(2) == [2, 1]


def test_seven():
    """Collatz sequence starting from 7."""
    assert solve(7) == [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


def test_three():
    """Collatz sequence starting from 3."""
    assert solve(3) == [3, 10, 5, 16, 8, 4, 2, 1]
