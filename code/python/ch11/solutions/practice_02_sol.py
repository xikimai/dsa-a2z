"""
Solution for Practice 2: Missing Number
============================================
Chapter 11: Hashing — The Secret Decoder Ring

APPROACH
--------
Add all numbers to a hash set. Then check each number from 0 to n —
the one not in the set is the missing number.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n) for the hash set
"""


def solve(nums: list[int]) -> int:
    """Find the missing number in [0, n]."""
    num_set = set(nums)
    n = len(nums)
    for i in range(n + 1):
        if i not in num_set:
            return i
    return -1  # should never reach here


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(solve(nums))
