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
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0:
            break

        target = -nums[i]
        left, right = i + 1, n - 1

        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif two_sum < target:
                left += 1
            else:
                right -= 1

    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        nums = list(map(int, line.split()))
    else:
        nums = []
    print(solve(nums))
