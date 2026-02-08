"""
Solution for Challenge 2: Maximum Subarray Sum Three Ways
==========================================================
Chapter 14: Prefix Sums — The Running Total Trick

APPROACH
--------
Three methods with decreasing time complexity.

TIME/SPACE:
  solve_brute:  O(n^3) / O(1)
  solve_prefix: O(n^2) / O(n)
  solve_kadane: O(n)   / O(1)
"""


def solve_brute(arr: list[int]) -> int:
    """O(n^3) brute force: try every subarray, sum each one."""
    pass  # TODO: Replace this with your solution


def solve_prefix(arr: list[int]) -> int:
    """O(n^2) prefix sum: precompute prefix, try all (l, r) pairs."""
    pass  # TODO: Replace this with your solution


def solve_kadane(arr: list[int]) -> int:
    """O(n) Kadane's: extend-or-restart in one pass."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    b = solve_brute(arr)
    p = solve_prefix(arr)
    k = solve_kadane(arr)
    print(f"brute={b} prefix={p} kadane={k}")

