"""
Solution for Challenge 2: Generate All Permutations
============================================
Chapter 10: The Magic of Recursion

APPROACH
--------
Sort the input first. Use backtracking: maintain a "used" boolean array.
At each recursion level, try each unused element, mark it used, recurse,
then unmark it (backtrack). Because input is sorted and we iterate in
order, the permutations are generated in lexicographic order.

TIME COMPLEXITY:  O(n! * n) — n! permutations, each takes O(n) to build
SPACE COMPLEXITY: O(n! * n) — storing all permutations
"""


def solve(nums: list[int]) -> list[list[int]]:
    """Generate all permutations, sorted lexicographically."""
    nums = sorted(nums)
    result = []
    used = [False] * len(nums)

    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                current.append(nums[i])
                backtrack(current)
                current.pop()
                used[i] = False

    backtrack([])
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split())) if input().strip() else []
    result = solve(data)
    for perm in result:
        print(perm)
