"""
Tests for Warmup 3: First Non-Repeating Character
========================================
Chapter 11: Hashing — The Secret Decoder Ring

Run with:
    python -m pytest code/python/ch11/tests/test_warmup_03.py -v
"""
from ch11.practice.warmup_03_first_non_repeating import solve


def test_basic():
    assert solve("aabbcdd") == "c"


def test_none():
    assert solve("aabb") == "_"


def test_all_twice():
    assert solve("abcabc") == "_"


def test_last_char():
    assert solve("aabbc") == "c"


def test_single():
    assert solve("a") == "a"


def test_empty():
    assert solve("") == "_"
