"""
Solution for Challenge 3: Number of Islands II
================================================
Chapter 29: Union-Find & Minimum Spanning Trees

APPROACH
--------
Online Union-Find: for each new land position, create a new component,
then try to union with 4-directional neighbors that are already land.

TIME COMPLEXITY:  O(K * alpha(m*n)) where K = len(positions)
SPACE COMPLEXITY: O(m * n)
"""


def solve(m: int, n: int, positions: list[list[int]]) -> list[int]:
    """Return island count after each land addition."""
    parent = {}
    rank = {}
    count = 0
    result = []

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        nonlocal count
        rx, ry = find(x), find(y)
        if rx == ry:
            return
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        count -= 1

    for r, c in positions:
        key = (r, c)
        if key in parent:
            # Duplicate position, count stays the same
            result.append(count)
            continue
        parent[key] = key
        rank[key] = 0
        count += 1
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            nkey = (nr, nc)
            if nkey in parent:
                union(key, nkey)
        result.append(count)

    return result


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    m = int(tokens[idx]); idx += 1
    n = int(tokens[idx]); idx += 1
    p = int(tokens[idx]); idx += 1
    positions = []
    for _ in range(p):
        r = int(tokens[idx]); idx += 1
        c = int(tokens[idx]); idx += 1
        positions.append([r, c])
    result = solve(m, n, positions)
    print(" ".join(map(str, result)))
