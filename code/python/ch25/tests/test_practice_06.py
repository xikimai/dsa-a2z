"""
Tests for Practice 6: Wildcard Matching
==========================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

Run with:
    python -m pytest code/python/ch25/tests/test_practice_06.py -v
"""
from ch25.practice.practice_06_wildcard_matching import solve


def test_no_match():
    assert solve("aa", "a") is False


def test_star_all():
    assert solve("aa", "*") is True


def test_question_fail():
    assert solve("cb", "?a") is False


def test_star_match():
    assert solve("adceb", "*a*b") is True


def test_empty_both():
    assert solve("", "") is True


def test_empty_star():
    assert solve("", "*") is True


def test_empty_pattern():
    assert solve("a", "") is False
