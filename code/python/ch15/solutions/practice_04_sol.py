"""
Solution for Practice 4: Subarray Sum Equals K (Sliding Window)
================================================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

APPROACH
--------
Variable sliding window for positive integers. Expand right to increase
sum. When sum exceeds k, shrink left. When sum equals k, count it and
shrink to continue searching.

TIME COMPLEXITY:  O(n) — each element enters/leaves window at most once
SPACE COMPLEXITY: O(1) — constant extra space
"""


def solve(arr: list[int], k: int) -> int:
    """Return count of subarrays with sum equal to k."""
    left = 0
    current_sum = 0
    count = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > k and left <= right:
            current_sum -= arr[left]
            left += 1

        if current_sum == k:
            count += 1

    return count


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    arr = list(map(int, line.split()))
    k = int(input().strip())
    print(solve(arr, k))
