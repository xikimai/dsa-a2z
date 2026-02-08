"""
Solution for Practice 2: Toggle i-th Bit
==========================================
Chapter 12: Bit Manipulation — The Language of Computers

APPROACH
--------
XOR n with (1 << i). XOR toggles the bit:
  - If bit i is 0, XOR with 1 makes it 1.
  - If bit i is 1, XOR with 1 makes it 0.

TIME COMPLEXITY:  O(1)
SPACE COMPLEXITY: O(1)
"""


def solve(n: int, i: int) -> int:
    """Return n with the i-th bit toggled."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().strip().split()
    n, i = int(parts[0]), int(parts[1])
    print(solve(n, i))

