"""
Tests for Practice 4: Letter Combinations of a Phone Number
Run with: python -m pytest code/python/ch13/tests/test_practice_04.py -v
"""
from ch13.practice.practice_04_letter_combinations import solve


def test_two_digits():
    assert solve("23") == [
        "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"
    ]


def test_single_digit():
    assert solve("2") == ["a", "b", "c"]


def test_empty():
    assert solve("") == []


def test_digit_7():
    assert solve("7") == ["p", "q", "r", "s"]


def test_three_digits():
    result = solve("234")
    assert len(result) == 27  # 3 * 3 * 3
    assert result[0] == "adg"
    assert result[-1] == "cfi"


def test_digit_9():
    assert solve("9") == ["w", "x", "y", "z"]
