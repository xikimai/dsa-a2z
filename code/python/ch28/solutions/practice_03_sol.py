"""
Solution for Practice 3: Find All Recipes
===========================================
Chapter 28: Topological Sort — Ordering Dependencies

APPROACH
--------
Model as a graph: each ingredient/recipe is a node. Edges from
ingredient to recipe. Supplies start with in-degree 0 (available).
Use Kahn's-like BFS. Recipes that get processed are makeable.

TIME COMPLEXITY:  O(V + E) where V = recipes + ingredients, E = total ingredient refs
SPACE COMPLEXITY: O(V + E)
"""

from collections import deque, defaultdict


def solve(recipes: list[str], ingredients: list[list[str]],
          supplies: list[str]) -> list[str]:
    """Return list of recipes that can be created."""
    recipe_set = set(recipes)
    in_degree = defaultdict(int)
    adj = defaultdict(list)

    for i, recipe in enumerate(recipes):
        for ing in ingredients[i]:
            adj[ing].append(recipe)
            in_degree[recipe] += 1

    queue = deque()
    for s in supplies:
        queue.append(s)

    result = []
    seen = set(supplies)
    while queue:
        item = queue.popleft()
        if item in recipe_set:
            result.append(item)
        for nxt in adj[item]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0 and nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)

    return result


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
