"""
Solution for Practice 3: Product of Array Except Self
======================================================
Chapter 14: Prefix Sums — The Running Total Trick

APPROACH
--------
Two-pass approach without division:
  1. Build left_products: left_products[i] = product of arr[0..i-1]
  2. Build right_products: right_products[i] = product of arr[i+1..n-1]
  3. result[i] = left_products[i] * right_products[i]

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n) — output array (can optimize to O(1) extra)
"""


def solve(arr: list[int]) -> list[int]:
    """Return array of products except self, without using division."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))

