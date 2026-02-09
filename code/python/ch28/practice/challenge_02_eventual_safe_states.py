"""
Challenge 2: Find Eventual Safe States
======================================
Chapter 28: Topological Sort — Ordering Dependencies

PROBLEM
-------
Return sorted list of safe nodes.

EXAMPLES
--------
  solve([[1, 2], [2, 3], [5], [0], [5], [], []]) -> [2, 4, 5, 6]
  solve([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]) -> [4]
  solve([[1], [2], []]) -> [0, 1, 2]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Three-color DFS. A node is safe if and only if it does not participate in any cycle. Nodes that finish as BLACK (fully

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(graph: list[list[int]]) -> list[int]:
    """Return sorted list of safe nodes."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = sys.stdin.read().strip()
    graph = json.loads(data)
    print(solve(graph))
