"""
Solution for Challenge 2: Trapping Rain Water
===============================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

APPROACH
--------
Two pointers from both ends. Track left_max and right_max.
Process the side with the smaller max — water level there is known.

TIME COMPLEXITY:  O(n) — single pass
SPACE COMPLEXITY: O(1) — constant extra space
"""


def solve(heights: list[int]) -> int:
    """Return total units of water trapped."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))

