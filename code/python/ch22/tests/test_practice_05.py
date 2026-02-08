"""
Tests for Practice 5: Remove All Adjacent Duplicates in String
==================================================================
Chapter 22: Stacks & Queues — Order Matters

Run with:
    python -m pytest code/python/ch22/tests/test_practice_05.py -v
"""
from ch22.practice.practice_05_remove_adjacent_duplicates import solve


def test_basic():
    assert solve("abbaca") == "ca"


def test_chain_removal():
    assert solve("azxxzy") == "ay"


def test_no_duplicates():
    assert solve("abc") == "abc"


def test_all_duplicates():
    assert solve("aabbcc") == ""


def test_single_char():
    assert solve("a") == "a"


def test_pair():
    assert solve("aa") == ""


def test_nested():
    assert solve("abba") == ""
