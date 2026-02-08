"""
Tests for Challenge 1: Reorganize String
===========================================
Chapter 17: Heaps & Priority Queues — The VIP Line

Run with:
    python -m pytest code/python/ch17/tests/test_challenge_01.py -v
"""
from ch17.practice.challenge_01_reorganize_string import solve


def _is_valid(s: str) -> bool:
    """Check that no two adjacent characters are the same."""
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return False
    return True


def _has_same_chars(original: str, result: str) -> bool:
    """Check that result has the same character counts."""
    return sorted(original) == sorted(result)


def test_basic():
    result = solve("aab")
    assert _is_valid(result) and _has_same_chars("aab", result)


def test_impossible():
    assert solve("aaab") == ""


def test_single_char():
    assert solve("a") == "a"


def test_two_chars():
    result = solve("ab")
    assert _is_valid(result) and _has_same_chars("ab", result)


def test_longer():
    result = solve("aaabbbccc")
    assert _is_valid(result) and _has_same_chars("aaabbbccc", result)


def test_all_same():
    assert solve("aaaa") == ""


def test_just_possible():
    # 3 a's in length 5 string -> (5+1)//2 = 3, so just possible
    result = solve("aabbc")
    assert _is_valid(result) and _has_same_chars("aabbc", result)
