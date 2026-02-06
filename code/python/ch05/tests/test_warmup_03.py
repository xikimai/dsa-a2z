"""
Tests for Warmup 3: Count Vowels
========================================
Chapter 5: Collections

Run with:
    python -m pytest code/python/ch05/tests/test_warmup_03.py -v
"""

from ch05.practice.warmup_03_count_vowels import solve


def test_mixed_case():
    """Hello World has 3 vowels (e, o, o)."""
    assert solve("Hello World") == 3


def test_all_vowels_lower():
    """All lowercase vowels."""
    assert solve("aeiou") == 5


def test_no_vowels():
    """No vowels in the string."""
    assert solve("xyz") == 0


def test_empty_string():
    """Empty string has zero vowels."""
    assert solve("") == 0


def test_all_vowels_upper():
    """All uppercase vowels."""
    assert solve("AEIOU") == 5


def test_no_vowels_consonants_only():
    """Word with no vowels."""
    assert solve("rhythm") == 0
