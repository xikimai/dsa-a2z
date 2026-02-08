"""
Solution for Challenge 1: Three Sum
=====================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

APPROACH
--------
Sort array. For each element nums[i], use two pointers on the
remaining elements to find pairs summing to -nums[i]. Skip
duplicates at all three levels.

TIME COMPLEXITY:  O(n^2) — outer loop O(n) * inner two-pointer O(n)
SPACE COMPLEXITY: O(1) extra beyond sorting and result list
"""


def solve(nums: list[int]) -> list[list[int]]:
    """Return sorted list of unique triplets that sum to zero."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        nums = list(map(int, line.split()))
    else:
        nums = []
    print(solve(nums))

