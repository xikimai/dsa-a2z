"""
Solution for Practice 4: Binary Search (Recursive)
============================================
Chapter 10: The Magic of Recursion

APPROACH
--------
Use a helper with lo and hi bounds.
Standard binary search: compute mid, compare with target,
recurse on the appropriate half.

TIME COMPLEXITY:  O(log n)
SPACE COMPLEXITY: O(log n) — recursion stack depth
"""


def solve(arr: list[int], target: int) -> int:
    """Binary search using recursion. Return index or -1."""
    def helper(lo, hi):
        if lo > hi:
            return -1
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return helper(mid + 1, hi)
        else:
            return helper(lo, mid - 1)

    return helper(0, len(arr) - 1)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    target = int(input())
    print(solve(data, target))
