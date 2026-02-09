"""
Solution for Practice 1: Number of Provinces
==============================================
Chapter 29: Union-Find & Minimum Spanning Trees

APPROACH
--------
Union-Find on the adjacency matrix. For each pair (i,j) where isConnected[i][j]=1,
union them. Count distinct roots at the end.

TIME COMPLEXITY:  O(n^2 * alpha(n))
SPACE COMPLEXITY: O(n)
"""


def solve(isConnected: list[list[int]]) -> int:
    """Return the number of provinces (connected components)."""
    n = len(isConnected)
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True

    components = n
    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                if union(i, j):
                    components -= 1
    return components


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(tokens[idx])); idx += 1
        matrix.append(row)
    print(solve(matrix))
