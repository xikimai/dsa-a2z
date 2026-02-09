"""
Practice 3: Find All Recipes
============================
Chapter 28: Topological Sort — Ordering Dependencies

PROBLEM
-------
Return list of recipes that can be created.

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Model as a graph: each ingredient/recipe is a node. Edges from ingredient to recipe. Supplies start with in-degree 0 (available).

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from collections import deque, defaultdict


def solve(recipes: list[str], ingredients: list[list[str]],
          supplies: list[str]) -> list[str]:
    """Return list of recipes that can be created."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = sys.stdin.read()
    lines = data.strip().split("\n")
    recipes = json.loads(lines[0])
    ingredients = json.loads(lines[1])
    supplies = json.loads(lines[2])
    print(solve(recipes, ingredients, supplies))
