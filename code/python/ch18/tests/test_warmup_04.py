"""
Tests for Warmup 4: Lemonade Change
======================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

Run with:
    python -m pytest code/python/ch18/tests/test_warmup_04.py -v
"""
from ch18.practice.warmup_04_lemonade_change import solve


def test_basic_true():
    assert solve([5, 5, 5, 10, 20]) is True


def test_basic_false():
    assert solve([5, 5, 10, 10, 20]) is False


def test_all_fives():
    assert solve([5, 5, 5]) is True


def test_single_five():
    assert solve([5]) is True


def test_ten_no_change():
    assert solve([10]) is False


def test_twenty_no_change():
    assert solve([20]) is False


def test_complex_true():
    assert solve([5, 5, 10, 5, 5, 20]) is True


def test_three_fives_then_twenty():
    assert solve([5, 5, 5, 20]) is True
