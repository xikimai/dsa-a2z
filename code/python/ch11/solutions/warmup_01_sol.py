"""
Solution for Warmup 1: Frequency Count
============================================
Chapter 11: Hashing — The Secret Decoder Ring

APPROACH
--------
Build a frequency dictionary by iterating through the array.
Convert to a list of [value, count] pairs and sort by value.

TIME COMPLEXITY:  O(n log n) — sorting the unique keys
SPACE COMPLEXITY: O(n) — frequency dictionary
"""


def solve(arr: list[int]) -> list[list[int]]:
    """Return sorted list of [value, count] pairs."""
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    result = [[val, cnt] for val, cnt in freq.items()]
    result.sort(key=lambda pair: pair[0])
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))
