"""
Solution for Warmup 2: Course Schedule I
==========================================
Chapter 28: Topological Sort — Ordering Dependencies

APPROACH
--------
Build directed graph from prerequisites: [a,b] means b -> a.
Use Kahn's algorithm. If all nodes are processed, no cycle exists.

TIME COMPLEXITY:  O(V + E)
SPACE COMPLEXITY: O(V + E)
"""

from collections import deque, defaultdict


def solve(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """Return True if all courses can be finished, False otherwise."""
    adj = defaultdict(list)
    in_degree = [0] * numCourses
    for a, b in prerequisites:
        adj[b].append(a)
        in_degree[a] += 1

    queue = deque()
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)

    count = 0
    while queue:
        u = queue.popleft()
        count += 1
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return count == numCourses


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    m = int(tokens[idx]); idx += 1
    prereqs = []
    for _ in range(m):
        a = int(tokens[idx]); idx += 1
        b = int(tokens[idx]); idx += 1
        prereqs.append([a, b])
    print(solve(n, prereqs))
