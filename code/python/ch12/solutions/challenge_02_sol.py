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
    xor_all = 0
    for x in nums:
        xor_all ^= x

    # Isolate lowest set bit (where a and b differ)
    diff_bit = xor_all & (-xor_all)

    a, b = 0, 0
    for x in nums:
        if x & diff_bit:
            a ^= x
        else:
            b ^= x

    return sorted([a, b])


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    print(solve(nums))
