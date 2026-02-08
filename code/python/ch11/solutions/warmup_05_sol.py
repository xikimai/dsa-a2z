"""
Solution for Warmup 5: Array Intersection
============================================
Chapter 11: Hashing — The Secret Decoder Ring

APPROACH
--------
Convert both arrays to sets, compute the intersection, and return
the result as a sorted list.

TIME COMPLEXITY:  O(n + m + k log k) where k = size of intersection
SPACE COMPLEXITY: O(n + m) for the two sets
"""


def solve(a: list[int], b: list[int]) -> list[int]:
    """Return sorted list of unique common elements."""
    set_a = set(a)
    set_b = set(b)
    return sorted(set_a & set_b)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line1 = input().strip()
    line2 = input().strip()
    a = list(map(int, line1.split())) if line1 else []
    b = list(map(int, line2.split())) if line2 else []
    print(solve(a, b))
