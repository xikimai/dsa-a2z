"""
Solution for Challenge 4: Minimum Operations to Make All Elements Equal
========================================================================
Chapter 14: Prefix Sums — The Running Total Trick

APPROACH
--------
Sort the array, then use prefix sums to compute the cost of making
all elements equal to arr[i] in O(1) per candidate.
For target arr[i]:
  left_cost  = i * arr[i] - prefix[i]
  right_cost = (prefix[n] - prefix[i+1]) - (n - i - 1) * arr[i]
Try all candidates, take the minimum.

TIME COMPLEXITY:  O(n log n) — dominated by sort (O(n) if already sorted)
SPACE COMPLEXITY: O(n) — prefix array
"""


def solve(arr: list[int]) -> int:
    """Return minimum operations to make all elements equal."""
    arr.sort()
    n = len(arr)
    if n <= 1:
        return 0

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    min_cost = float("inf")
    for i in range(n):
        left_cost = i * arr[i] - prefix[i]
        right_cost = (prefix[n] - prefix[i + 1]) - (n - i - 1) * arr[i]
        total_cost = left_cost + right_cost
        min_cost = min(min_cost, total_cost)

    return min_cost


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))
