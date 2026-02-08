"""
Tests for Practice 2: Evaluate Reverse Polish Notation
==========================================================
Chapter 22: Stacks & Queues — Order Matters

Run with:
    python -m pytest code/python/ch22/tests/test_practice_02.py -v
"""
from ch22.practice.practice_02_eval_rpn import solve


def test_addition_and_multiply():
    assert solve(["2", "1", "+", "3", "*"]) == 9


def test_division():
    assert solve(["4", "13", "5", "/", "+"]) == 6


def test_complex():
    assert solve(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22


def test_single_number():
    assert solve(["42"]) == 42


def test_subtraction():
    assert solve(["5", "3", "-"]) == 2


def test_negative_division():
    # 6 / -132 truncates toward zero = 0
    assert solve(["6", "-132", "/"]) == 0


def test_negative_result():
    assert solve(["3", "5", "-"]) == -2
