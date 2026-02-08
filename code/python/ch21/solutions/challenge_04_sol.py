"""
Solution for Challenge 4: Flatten a Multilevel Doubly Linked List
==================================================================
Chapter 21: Linked Lists — Pointers and Connections

APPROACH
--------
Use recursion: for each element, if it's a list, recursively flatten
it; if it's an integer, add it to the result.

TIME COMPLEXITY:  O(n) where n is total number of integers
SPACE COMPLEXITY: O(d) where d is nesting depth (recursion stack)
"""


def solve(nested: list) -> list[int]:
    """Flatten the nested list into a single-level list (depth-first)."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(solve(item))
        else:
            result.append(item)
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json
    nested = json.loads(input().strip())
    print(solve(nested))
