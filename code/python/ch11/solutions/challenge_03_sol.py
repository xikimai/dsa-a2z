"""
Solution for Challenge 3: Repeating and Missing Number
============================================
Chapter 11: Hashing — The Secret Decoder Ring

APPROACH
--------
Use a hash set. Iterate through the array — if a number is already in
the set, it's the repeating number. Then check 1..n to find the number
not present in the set (the missing number).

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n) for the hash set
"""


def solve(nums: list[int]) -> list[int]:
    """Return [repeating_number, missing_number]."""
    n = len(nums)
    seen = set()
    repeating = -1

    for num in nums:
        if num in seen:
            repeating = num
        seen.add(num)

    missing = -1
    for i in range(1, n + 1):
        if i not in seen:
            missing = i
            break

    return [repeating, missing]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(solve(nums))
