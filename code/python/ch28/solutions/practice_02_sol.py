"""
Solution for Practice 2: Parallel Courses
===========================================
Chapter 28: Topological Sort — Ordering Dependencies

APPROACH
--------
Level-based Kahn's BFS (1-indexed nodes).
Count BFS levels = minimum semesters.

TIME COMPLEXITY:  O(V + E)
SPACE COMPLEXITY: O(V + E)
"""

from collections import deque, defaultdict


def solve(n: int, relations: list[list[int]]) -> int:
    """Return minimum semesters to complete all courses, or -1 if impossible."""
    adj = defaultdict(list)
    in_degree = [0] * (n + 1)
    for prev, nxt in relations:
        adj[prev].append(nxt)
        in_degree[nxt] += 1

    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    semesters = 0
    count = 0
    while queue:
        semesters += 1
        for _ in range(len(queue)):
            u = queue.popleft()
            count += 1
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

    return semesters if count == n else -1


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    m = int(tokens[idx]); idx += 1
    relations = []
    for _ in range(m):
        a = int(tokens[idx]); idx += 1
        b = int(tokens[idx]); idx += 1
        relations.append([a, b])
    print(solve(n, relations))
