"""
Tests for Warmup 4: Repeat String
========================================
Chapter 4: Functions

Run with:
    python -m pytest code/python/ch04/tests/test_warmup_04.py -v
"""

from ch04.practice.warmup_04_repeat_string import solve


def test_default_repeat():
    """Default n=3 repetition."""
    assert solve("ha") == "ha ha ha"


def test_repeat_five():
    """Repeat 5 times."""
    assert solve("yo", 5) == "yo yo yo yo yo"


def test_repeat_one():
    """Repeat once — just the string itself."""
    assert solve("!", 1) == "!"


def test_repeat_zero():
    """Repeat zero times — empty string."""
    assert solve("x", 0) == ""


def test_repeat_with_spaces():
    """String that already contains spaces."""
    assert solve("hi there", 2) == "hi there hi there"


def test_single_char():
    """Single character repeated."""
    assert solve("a", 4) == "a a a a"
