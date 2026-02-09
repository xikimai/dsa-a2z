"""
Solution for Challenge 2: Find Eventual Safe States
=====================================================
Chapter 28: Topological Sort — Ordering Dependencies

APPROACH
--------
Three-color DFS. A node is safe if and only if it does not
participate in any cycle. Nodes that finish as BLACK (fully
processed without finding a cycle) are safe.

TIME COMPLEXITY:  O(V + E)
SPACE COMPLEXITY: O(V + E)
"""


def solve(graph: list[list[int]]) -> list[int]:
    """Return sorted list of safe nodes."""
    n = len(graph)
    color = [0] * n  # 0=white, 1=gray, 2=black

    def is_safe(u):
        if color[u] == 1:
            return False  # cycle
        if color[u] == 2:
            return True   # already determined safe
        color[u] = 1  # gray
        for v in graph[u]:
            if not is_safe(v):
                return False
        color[u] = 2  # black = safe
        return True

    return [i for i in range(n) if is_safe(i)]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = sys.stdin.read().strip()
    graph = json.loads(data)
    print(solve(graph))
