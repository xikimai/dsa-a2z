"""
Solution for Warmup 1: Pair Sum in Sorted Array
=================================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

APPROACH
--------
Use converging two pointers from both ends of the sorted array.
If sum < target, move left pointer right. If sum > target, move right left.

TIME COMPLEXITY:  O(n) — each pointer moves at most n steps total
SPACE COMPLEXITY: O(1) — only pointer variables
"""


def solve(arr: list[int], target: int) -> list[int]:
    """Return pair [a, b] that sums to target, or [-1, -1]."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    target = int(input().strip())
    print(solve(arr, target))

