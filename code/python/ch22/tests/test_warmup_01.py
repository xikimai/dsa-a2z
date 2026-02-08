"""
Tests for Warmup 1: Valid Parentheses
=========================================
Chapter 22: Stacks & Queues — Order Matters

Run with:
    python -m pytest code/python/ch22/tests/test_warmup_01.py -v
"""
from ch22.practice.warmup_01_valid_parentheses import solve


def test_simple_valid():
    assert solve("()") is True


def test_multiple_types():
    assert solve("()[]{}") is True


def test_nested():
    assert solve("{[]}") is True


def test_interleaved_invalid():
    assert solve("([)]") is False


def test_unmatched_open():
    assert solve("(((") is False


def test_unmatched_close():
    assert solve(")") is False


def test_empty():
    assert solve("") is True


def test_complex_valid():
    assert solve("({[(){}]})") is True


def test_single_open():
    assert solve("(") is False


def test_wrong_close():
    assert solve("(]") is False
