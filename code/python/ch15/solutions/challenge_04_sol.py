"""
Solution for Challenge 4: Fruit Into Baskets (Max Two Distinct Types)
======================================================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

APPROACH
--------
Sliding window with hash map tracking fruit type counts. When more
than 2 distinct types are in the window, shrink from left until
we're back to at most 2.

TIME COMPLEXITY:  O(n) — each element enters/leaves window once
SPACE COMPLEXITY: O(1) — at most 3 entries in the hash map
"""


def solve(fruits: list[int]) -> int:
    """Return maximum fruits collectible with 2 baskets."""
    freq = {}
    left = 0
    best = 0

    for right in range(len(fruits)):
        fruit = fruits[right]
        freq[fruit] = freq.get(fruit, 0) + 1

        while len(freq) > 2:
            left_fruit = fruits[left]
            freq[left_fruit] -= 1
            if freq[left_fruit] == 0:
                del freq[left_fruit]
            left += 1

        best = max(best, right - left + 1)

    return best


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    arr = list(map(int, line.split()))
    print(solve(arr))
