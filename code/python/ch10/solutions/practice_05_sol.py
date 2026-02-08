"""
Solution for Practice 5: Generate All Subsets
============================================
Chapter 10: The Magic of Recursion

APPROACH
--------
Sort the input first for deterministic output.
Use backtracking: at each index, choose to include or exclude the
current element. When we reach the end, record the current subset.
Finally, sort the result by length first, then lexicographically.

TIME COMPLEXITY:  O(2^n * n) — 2^n subsets, each up to length n
SPACE COMPLEXITY: O(2^n * n) — storing all subsets
"""


def solve(nums: list[int]) -> list[list[int]]:
    """Generate all subsets, sorted by length then lexicographically."""
    nums = sorted(nums)
    result = []

    def backtrack(index, current):
        if index == len(nums):
            result.append(current[:])
            return
        # Include nums[index]
        current.append(nums[index])
        backtrack(index + 1, current)
        current.pop()
        # Exclude nums[index]
        backtrack(index + 1, current)

    backtrack(0, [])
    result.sort(key=lambda s: (len(s), s))
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split())) if input().strip() else []
    result = solve(data)
    for subset in result:
        print(subset)
