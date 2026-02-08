"""
Solution for Warmup 4: Is Array Prefix of Another
===================================================
Chapter 14: Prefix Sums — The Running Total Trick

APPROACH
--------
Check length constraint, then compare element by element.

TIME COMPLEXITY:  O(min(n, m))
SPACE COMPLEXITY: O(1)
"""


def solve(arr1: list[int], arr2: list[int]) -> bool:
    """Return True if arr1 is a prefix of arr2."""
    if len(arr1) > len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line1 = input().strip()
    line2 = input().strip()
    arr1 = list(map(int, line1.split())) if line1 else []
    arr2 = list(map(int, line2.split())) if line2 else []
    print(solve(arr1, arr2))
