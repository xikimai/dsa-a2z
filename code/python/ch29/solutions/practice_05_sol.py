"""
Solution for Practice 5: Satisfiability of Equality Equations
==============================================================
Chapter 29: Union-Find & Minimum Spanning Trees

APPROACH
--------
First pass: process all "==" equations and union the variables.
Second pass: process all "!=" equations and check if they conflict.

TIME COMPLEXITY:  O(n * alpha(26)) = O(n)
SPACE COMPLEXITY: O(1) — only 26 letters
"""


def solve(equations: list[str]) -> bool:
    """Return True if all equations can be satisfied simultaneously."""
    parent = list(range(26))
    rank = [0] * 26

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

    # First pass: union all "==" pairs
    for eq in equations:
        if eq[1] == '=':
            a = ord(eq[0]) - ord('a')
            b = ord(eq[3]) - ord('a')
            union(a, b)

    # Second pass: check all "!=" pairs
    for eq in equations:
        if eq[1] == '!':
            a = ord(eq[0]) - ord('a')
            b = ord(eq[3]) - ord('a')
            if find(a) == find(b):
                return False

    return True


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip().split()
    print(solve(data))
