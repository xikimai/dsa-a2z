"""
Tests for Practice 1: Alien Dictionary
========================================
Chapter 28: Topological Sort — Ordering Dependencies

Run with:
    python -m pytest code/python/ch28/tests/test_practice_01.py -v
"""
from ch28.practice.practice_01_alien_dictionary import solve


def is_valid_alien_order(words, order):
    """Validate that the order is consistent with the word ordering."""
    if not order:
        return False
    pos = {c: i for i, c in enumerate(order)}
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        found_diff = False
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if pos.get(c1, -1) >= pos.get(c2, -1):
                    return False
                found_diff = True
                break
        if not found_diff and len(w1) > len(w2):
            return False
    return True


def test_basic():
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    result = solve(words)
    assert is_valid_alien_order(words, result)


def test_two_words():
    words = ["z", "x"]
    result = solve(words)
    assert is_valid_alien_order(words, result)


def test_cycle():
    assert solve(["z", "x", "z"]) == ""


def test_prefix_conflict():
    assert solve(["abc", "ab"]) == ""
