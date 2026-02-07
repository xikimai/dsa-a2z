"""
Solution for Challenge 3: Sum of GCD Pairs
============================================
Chapter 7: Number Wizardry — Math for Programmers

APPROACH
--------
Brute force: for all pairs i < j, compute GCD and sum.
Uses Euclidean algorithm for each GCD.

TIME COMPLEXITY:  O(n^2 * log(max_val))
SPACE COMPLEXITY: O(1)
"""


def solve(nums: list[int]) -> int:
    """Return the sum of GCD(nums[i], nums[j]) for all i < j."""
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    total = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            total += gcd(nums[i], nums[j])
    return total


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(solve(nums))
