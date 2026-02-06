"""
Solution for Warmup 04: Swap Two Numbers
============================================
Chapter 2: Your First Programs

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
In Python, swapping is elegant — just return (b, a). Python lets you
create tuples on the fly. In other languages you'd need a temporary
variable, but Python's tuple packing makes it a one-liner.

TIME COMPLEXITY:  O(1) — just creating a tuple
SPACE COMPLEXITY: O(1) — the tuple is constant size
"""


def solve(a: int, b: int) -> tuple[int, int]:
    """Return a tuple with a and b swapped."""
    return (b, a)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    a, b = map(int, input().split())
    result = solve(a, b)
    print(result[0], result[1])
