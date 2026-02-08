"""
Solution for Warmup 3: Running Sum of Array
=============================================
Chapter 14: Prefix Sums — The Running Total Trick

APPROACH
--------
Accumulate sum while iterating.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n) — the output array
"""


def solve(arr: list[int]) -> list[int]:
    """Return the running sum array (same length as input)."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))

