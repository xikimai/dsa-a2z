"""
Solution for Practice 4: Clone Graph
======================================
Chapter 19: Graphs I — Exploring Networks

APPROACH
--------
Create a new list of empty lists. Copy each node's neighbor list.
This ensures a deep copy where modifying the clone doesn't affect
the original.

TIME COMPLEXITY:  O(V + E)
SPACE COMPLEXITY: O(V + E)
"""


def solve(adj: list[list[int]]) -> list[list[int]]:
    """Return a deep clone of the adjacency list."""
    n = len(adj)
    clone = [[] for _ in range(n)]
    for i in range(n):
        clone[i] = list(adj[i])
    return clone


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    adj = []
    for _ in range(n):
        line = input().strip()
        if line:
            adj.append(list(map(int, line.split())))
        else:
            adj.append([])
    clone = solve(adj)
    for i in range(len(clone)):
        print(f"{i}: {clone[i]}")
