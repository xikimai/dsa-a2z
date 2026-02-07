"""
Tests for Warmup 5: Armstrong Number
========================================
Chapter 7: Number Wizardry — Math for Programmers

Run with:
    python -m pytest code/python/ch07/tests/test_warmup_05.py -v
"""

from ch07.practice.warmup_05_armstrong_number import solve


def test_153():
    assert solve(153) is True


def test_370():
    assert solve(370) is True


def test_9474():
    assert solve(9474) is True


def test_not_armstrong():
    assert solve(100) is False


def test_single_digit():
    assert solve(1) is True


def test_zero():
    assert solve(0) is True
