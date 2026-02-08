"""
Solution for Challenge 2: Two Numbers Appearing Odd Times
==========================================================
Chapter 12: Bit Manipulation — The Language of Computers

APPROACH
--------
1. XOR all elements -> xor_all = a ^ b
2. Find the lowest set bit of xor_all (this bit differs between a and b)
3. Partition elements by this bit, XOR each group to isolate a and b
4. Return sorted.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(nums: list[int]) -> list[int]:
    """Return sorted list of two odd-occurring elements."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    print(solve(nums))

