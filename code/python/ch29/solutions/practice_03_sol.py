"""
Solution for Practice 3: Most Stones Removed
==============================================
Chapter 29: Union-Find & Minimum Spanning Trees

APPROACH
--------
Two stones are connected if they share a row or column. Use Union-Find to
group stones by connectivity. The answer is total_stones - number_of_components
(we must leave one stone per component).

We map rows and columns to a shared Union-Find space using an offset for columns.

TIME COMPLEXITY:  O(n * alpha(n))
SPACE COMPLEXITY: O(n)
"""


def solve(stones: list[list[int]]) -> int:
    """Return the maximum number of stones that can be removed."""
    if not stones:
        return 0

    parent = {}
    rank = {}

    def find(x):
        if x not in parent:
            parent[x] = x
            rank[x] = 0
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

    # Use row as-is and column + offset to avoid collision
    # Offset columns by a large number to separate row/col namespace
    for r, c in stones:
        union(r, c + 10001)

    # Count unique components among the stones
    components = len({find(r) for r, c in stones})
    return len(stones) - components


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    stones = []
    for _ in range(n):
        r = int(tokens[idx]); idx += 1
        c = int(tokens[idx]); idx += 1
        stones.append([r, c])
    print(solve(stones))
