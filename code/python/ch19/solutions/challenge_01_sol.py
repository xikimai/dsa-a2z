"""
Solution for Challenge 1: Number of Provinces
===============================================
Chapter 19: Graphs I — Exploring Networks

APPROACH
--------
DFS/BFS on the adjacency matrix. For each unvisited city, run DFS
to mark all connected cities as visited. Count the number of DFS launches.

TIME COMPLEXITY:  O(n^2) — checking all entries in the matrix
SPACE COMPLEXITY: O(n)
"""

from collections import deque


def solve(isConnected: list[list[int]]) -> int:
    """Return the number of provinces."""
    n = len(isConnected)
    visited = [False] * n
    count = 0

    for i in range(n):
        if not visited[i]:
            # BFS from city i
            queue = deque([i])
            visited[i] = True
            while queue:
                city = queue.popleft()
                for j in range(n):
                    if isConnected[city][j] == 1 and not visited[j]:
                        visited[j] = True
                        queue.append(j)
            count += 1

    return count


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    isConnected = []
    for _ in range(n):
        row = list(map(int, input().strip().split()))
        isConnected.append(row)
    print(solve(isConnected))
