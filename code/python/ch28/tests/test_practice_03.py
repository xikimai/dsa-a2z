"""
Tests for Practice 3: Find All Recipes
========================================
Chapter 28: Topological Sort — Ordering Dependencies

Run with:
    python -m pytest code/python/ch28/tests/test_practice_03.py -v
"""
from ch28.practice.practice_03_find_all_recipes import solve


def test_chain():
    result = solve(
        ["bread", "sandwich"],
        [["yeast", "flour"], ["bread", "meat"]],
        ["yeast", "flour", "meat"]
    )
    assert sorted(result) == ["bread", "sandwich"]


def test_missing_ingredient():
    result = solve(
        ["bread"],
        [["yeast", "flour"]],
        ["yeast"]
    )
    assert result == []


def test_single_recipe():
    result = solve(
        ["cake"],
        [["flour", "sugar", "eggs"]],
        ["flour", "sugar", "eggs"]
    )
    assert result == ["cake"]


def test_circular_dependency():
    result = solve(
        ["a", "b"],
        [["b"], ["a"]],
        []
    )
    assert result == []
