"""
Solution for Challenge 2: Longest Consecutive Sequence
============================================
Chapter 11: Hashing — The Secret Decoder Ring

APPROACH
--------
Add all numbers to a hash set. For each number where (num - 1) is NOT
in the set (i.e., it's the start of a consecutive sequence), count how
many consecutive numbers follow. Track the maximum length.

TIME COMPLEXITY:  O(n) — each element visited at most twice
SPACE COMPLEXITY: O(n) for the hash set
"""


def solve(nums: list[int]) -> int:
    """Find length of longest consecutive sequence in O(n)."""
    if not nums:
        return 0

    num_set = set(nums)
    max_len = 0

    for num in num_set:
        # Only start counting from the beginning of a sequence
        if num - 1 not in num_set:
            current = num
            length = 1
            while current + 1 in num_set:
                current += 1
                length += 1
            max_len = max(max_len, length)

    return max_len


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        nums = list(map(int, line.split()))
    else:
        nums = []
    print(solve(nums))
