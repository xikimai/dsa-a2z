"""
Solution for Challenge 4: Smallest String With Swaps
=====================================================
Chapter 29: Union-Find & Minimum Spanning Trees

APPROACH
--------
Use Union-Find to group indices that are connected via swap pairs.
Within each group, sort the characters and place them back in sorted index order.

TIME COMPLEXITY:  O(n log n)
SPACE COMPLEXITY: O(n)
"""

from collections import defaultdict


def solve(s: str, pairs: list[list[int]]) -> str:
    """Return the lexicographically smallest string achievable by swapping."""
    n = len(s)
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
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

    for a, b in pairs:
        union(a, b)

    # Group indices by their root
    groups = defaultdict(list)
    for i in range(n):
        groups[find(i)].append(i)

    # Within each group, sort characters and assign back
    result = list(s)
    for indices in groups.values():
        chars = sorted(result[i] for i in indices)
        for i, c in zip(sorted(indices), chars):
            result[i] = c

    return "".join(result)


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip().split("\n")
    s = data[0]
    pairs = []
    for line in data[1:]:
        a, b = map(int, line.split())
        pairs.append([a, b])
    print(solve(s, pairs))
