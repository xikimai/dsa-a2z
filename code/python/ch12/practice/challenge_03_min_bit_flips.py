"""
Solution for Challenge 3: Minimum Bit Flips
=============================================
Chapter 12: Bit Manipulation — The Language of Computers

APPROACH
--------
XOR start and goal. The set bits in the result are exactly the bits
that differ. Count them using Brian Kernighan's algorithm.

TIME COMPLEXITY:  O(k) where k = number of differing bits
SPACE COMPLEXITY: O(1)
"""


def solve(start: int, goal: int) -> int:
    """Return minimum bit flips to convert start to goal."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().strip().split()
    start, goal = int(parts[0]), int(parts[1])
    print(solve(start, goal))

