"""
Tests for Practice 01: FizzBuzz
========================================
Chapter 3: Decisions and Loops

Run with:
    python -m pytest code/python/ch03/tests/test_practice_01.py -v
"""

from ch03.practice.practice_01_fizzbuzz import solve


def test_fifteen():
    """Classic FizzBuzz from 1 to 15."""
    expected = [
        "1", "2", "Fizz", "4", "Buzz",
        "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz",
    ]
    assert solve(15) == expected


def test_one():
    """FizzBuzz with just 1."""
    assert solve(1) == ["1"]


def test_five():
    """Last element of FizzBuzz(5) should be 'Buzz'."""
    result = solve(5)
    assert result[-1] == "Buzz"


def test_three():
    """FizzBuzz from 1 to 3."""
    assert solve(3) == ["1", "2", "Fizz"]
