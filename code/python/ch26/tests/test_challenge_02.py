"""
Tests for Challenge 2: Serialize and Deserialize
===================================================
Chapter 26: Trees — Branches of Logic

Run with:
    python -m pytest code/python/ch26/tests/test_challenge_02.py -v
"""
from ch26.practice.challenge_02_serialize import serialize, deserialize, build_tree, tree_to_list


def test_round_trip():
    tree = build_tree([1, 2, 3, None, None, 4, 5])
    s = serialize(tree)
    restored = deserialize(s)
    assert tree_to_list(restored) == [1, 2, 3, None, None, 4, 5]


def test_single():
    tree = build_tree([1])
    s = serialize(tree)
    restored = deserialize(s)
    assert tree_to_list(restored) == [1]


def test_empty():
    s = serialize(None)
    restored = deserialize(s)
    assert restored is None
