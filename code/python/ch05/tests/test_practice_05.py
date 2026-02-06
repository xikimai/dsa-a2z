"""
Tests for Practice 5: Longest Common Prefix
=============================================
Chapter 5: Collections

Run with:
    python -m pytest code/python/ch05/tests/test_practice_05.py -v
"""

from ch05.practice.practice_05_longest_common_prefix import solve


def test_common_prefix():
    """Strings share 'fl' as common prefix."""
    assert solve(["flower", "flow", "flight"]) == "fl"


def test_no_common_prefix():
    """No common prefix at all."""
    assert solve(["dog", "racecar", "car"]) == ""


def test_single_string():
    """Single string — the whole string is the prefix."""
    assert solve(["abc"]) == "abc"


def test_empty_string_in_list():
    """One empty string makes the prefix empty."""
    assert solve(["", "abc"]) == ""


def test_all_same():
    """All strings identical."""
    assert solve(["a", "a", "a"]) == "a"
