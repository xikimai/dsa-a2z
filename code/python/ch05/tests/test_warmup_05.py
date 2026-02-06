"""
Tests for Warmup 5: Character Frequency
========================================
Chapter 5: Collections

Run with:
    python -m pytest code/python/ch05/tests/test_warmup_05.py -v
"""

from ch05.practice.warmup_05_char_frequency import solve


def test_basic_frequency():
    """Simple string with repeated characters."""
    assert solve("aab") == {"a": 2, "b": 1}


def test_empty_string():
    """Empty string returns empty dict."""
    assert solve("") == {}


def test_all_unique():
    """All characters are unique."""
    assert solve("abc") == {"a": 1, "b": 1, "c": 1}


def test_all_same():
    """All characters are the same."""
    assert solve("aaa") == {"a": 3}


def test_with_spaces():
    """String with spaces — spaces count as characters."""
    result = solve("a b")
    assert result == {"a": 1, " ": 1, "b": 1}
