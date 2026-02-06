"""
Tests for Warmup 01: Greeting
========================================
Chapter 2: Your First Programs

Run with:
    python -m pytest code/python/ch02/tests/test_warmup_01.py -v
"""

from ch02.practice.warmup_01_greeting import solve


def test_greet_maya():
    """Greeting Maya should produce 'Hello, Maya!'."""
    assert solve("Maya") == "Hello, Maya!"


def test_greet_world():
    """Greeting World should produce 'Hello, World!'."""
    assert solve("World") == "Hello, World!"


def test_greet_single_char():
    """Greeting a single character name."""
    assert solve("A") == "Hello, A!"


def test_greet_long_name():
    """Greeting a longer name with spaces."""
    assert solve("John Doe") == "Hello, John Doe!"


def test_greet_lowercase():
    """Greeting a lowercase name."""
    assert solve("python") == "Hello, python!"
