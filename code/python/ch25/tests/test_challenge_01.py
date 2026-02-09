"""
Tests for Challenge 1: Shortest Common Supersequence
=======================================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

Run with:
    python -m pytest code/python/ch25/tests/test_challenge_01.py -v
"""
from ch25.practice.challenge_01_shortest_common_supersequence import solve


def _is_subsequence(s, t):
    """Check if s is a subsequence of t."""
    it = iter(t)
    return all(c in it for c in s)


def _validate_scs(str1, str2, result, expected_len):
    """Validate that result is a valid SCS of correct length."""
    assert len(result) == expected_len, (
        f"Expected length {expected_len}, got {len(result)} for '{result}'"
    )
    assert _is_subsequence(str1, result), (
        f"'{str1}' is not a subsequence of '{result}'"
    )
    assert _is_subsequence(str2, result), (
        f"'{str2}' is not a subsequence of '{result}'"
    )


def test_basic():
    result = solve("abac", "cab")
    _validate_scs("abac", "cab", result, 5)


def test_identical():
    result = solve("aaaaaaaa", "aaaaaaaa")
    _validate_scs("aaaaaaaa", "aaaaaaaa", result, 8)


def test_no_common():
    result = solve("abc", "xyz")
    _validate_scs("abc", "xyz", result, 6)


def test_one_char():
    result = solve("a", "b")
    _validate_scs("a", "b", result, 2)
