"""
Solution for Warmup 2: Highest and Lowest Frequency Element
============================================
Chapter 11: Hashing — The Secret Decoder Ring

APPROACH
--------
Build a frequency map. Find the element with the maximum frequency
and the element with the minimum frequency.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""


def solve(arr: list[int]) -> list[int]:
    """Return [element_with_highest_freq, element_with_lowest_freq]."""
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    highest = max(freq, key=freq.get)
    lowest = min(freq, key=freq.get)
    return [highest, lowest]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))
