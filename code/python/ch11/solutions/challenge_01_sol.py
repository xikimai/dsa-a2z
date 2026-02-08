"""
Solution for Challenge 1: Missing Number — Four Ways
============================================
Chapter 11: Hashing — The Secret Decoder Ring

APPROACH
--------
Four different approaches to find the missing number:
1. Sort: Sort array, scan for gap where nums[i] != i
2. XOR: XOR all elements with 0..n (duplicates cancel out)
3. Math: Expected sum n*(n+1)//2 minus actual sum
4. Hash: Hash set, check 0..n for missing

TIME COMPLEXITY:  Sort O(n log n), others O(n)
SPACE COMPLEXITY: Sort O(1)*, XOR O(1), Math O(1), Hash O(n)
"""


def solve_sort(nums: list[int]) -> int:
    """Find missing number using sort approach."""
    nums_sorted = sorted(nums)
    for i, num in enumerate(nums_sorted):
        if num != i:
            return i
    return len(nums)


def solve_xor(nums: list[int]) -> int:
    """Find missing number using XOR approach."""
    n = len(nums)
    xor_all = 0
    for i in range(n + 1):
        xor_all ^= i
    for num in nums:
        xor_all ^= num
    return xor_all


def solve_math(nums: list[int]) -> int:
    """Find missing number using math (sum) approach."""
    n = len(nums)
    expected = n * (n + 1) // 2
    actual = sum(nums)
    return expected - actual


def solve_hash(nums: list[int]) -> int:
    """Find missing number using hash set approach."""
    num_set = set(nums)
    n = len(nums)
    for i in range(n + 1):
        if i not in num_set:
            return i
    return -1  # should never reach here


def solve(nums: list[int]) -> int:
    """Default solve — uses the math approach."""
    return solve_math(nums)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(solve(nums))
