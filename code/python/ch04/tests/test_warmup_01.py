"""
Tests for Warmup 1: Greeting
========================================
Chapter 4: Functions

Run with:
    python -m pytest code/python/ch04/tests/test_warmup_01.py -v
"""

from ch04.practice.warmup_01_greeting import solve


def test_normal_name():
    """Basic greeting with a normal name."""
    assert solve("Alice") == "Hello, Alice!"


def test_another_name():
    """Basic greeting with another name."""
    assert solve("Bob") == "Hello, Bob!"


def test_empty_string():
    """Edge case: empty name still produces valid format."""
    assert solve("") == "Hello, !"


def test_name_with_spaces():
    """Name containing spaces."""
    assert solve("Mary Jane") == "Hello, Mary Jane!"


def test_single_character():
    """Single character name."""
    assert solve("X") == "Hello, X!"


def test_numbers_in_name():
    """Name containing numbers."""
    assert solve("Agent007") == "Hello, Agent007!"
