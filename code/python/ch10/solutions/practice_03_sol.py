"""
Solution for Practice 3: Count Occurrences
============================================
Chapter 10: The Magic of Recursion

APPROACH
--------
Use a helper with an index parameter.
Base case: index reaches end of array, return 0.
Count 1 if current element matches target, then recurse on next index.

TIME COMPLEXITY:  O(n) — visit each element once
SPACE COMPLEXITY: O(n) — recursion stack depth
"""


def solve(arr: list[int], target: int) -> int:
    """Count occurrences of target in arr, recursively."""
    def helper(idx):
        if idx == len(arr):
            return 0
        count = 1 if arr[idx] == target else 0
        return count + helper(idx + 1)

    return helper(0)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    target = int(input())
    print(solve(data, target))
