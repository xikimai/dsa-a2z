"""
Tests for Warmup 3: Check Power of Two
========================================
Chapter 12: Bit Manipulation — The Language of Computers

Run with:
    python -m pytest code/python/ch12/tests/test_warmup_03.py -v
"""
from ch12.practice.warmup_03_check_power_of_two import solve


def test_powers():
    for p in [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
        assert solve(p) is True, f"{p} should be power of 2"


def test_non_powers():
    for n in [3, 5, 6, 7, 9, 10, 12, 15, 100]:
        assert solve(n) is False, f"{n} should NOT be power of 2"


def test_zero():
    assert solve(0) is False


def test_negative():
    assert solve(-4) is False


def test_large_power():
    assert solve(2**20) is True


def test_large_non_power():
    assert solve(2**20 + 1) is False
