"""
Tests for Challenge 3: Minimum Platforms
==========================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

Run with:
    python -m pytest code/python/ch18/tests/test_challenge_03.py -v
"""
from ch18.practice.challenge_03_min_platforms import solve


def test_basic():
    assert solve(
        [900, 940, 950, 1100, 1500, 1800],
        [910, 1200, 1120, 1130, 1900, 2000]
    ) == 3


def test_no_overlap():
    assert solve([900, 1100, 1235], [1000, 1200, 1240]) == 1


def test_all_overlap():
    assert solve([100, 100, 100], [200, 200, 200]) == 3


def test_single():
    assert solve([900], [1000]) == 1


def test_two_overlap():
    assert solve([900, 940], [1000, 950]) == 2


def test_sequential():
    assert solve([100, 200, 300], [150, 250, 350]) == 1


def test_empty():
    assert solve([], []) == 0
