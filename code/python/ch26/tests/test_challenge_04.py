"""
Tests for Challenge 4: Binary Tree Cameras
=============================================
Chapter 26: Trees — Branches of Logic

Run with:
    python -m pytest code/python/ch26/tests/test_challenge_04.py -v
"""
from ch26.practice.challenge_04_cameras import solve, build_tree


def test_basic():
    assert solve(build_tree([0, 0, None, 0, 0])) == 1


def test_longer():
    assert solve(build_tree([0, 0, None, 0, None, 0, None, None, 0])) == 2
