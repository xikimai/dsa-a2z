"""
Solution for Practice 3: Set and Clear Bits
=============================================
Chapter 12: Bit Manipulation — The Language of Computers

APPROACH
--------
Set: OR with (1 << i) ensures the i-th bit is 1.
Clear: AND with ~(1 << i) ensures the i-th bit is 0.

TIME COMPLEXITY:  O(1) for both operations
SPACE COMPLEXITY: O(1)
"""


def solve_set(n: int, i: int) -> int:
    """Return n with the i-th bit set to 1."""
    pass  # TODO: Replace this with your solution


def solve_clear(n: int, i: int) -> int:
    """Return n with the i-th bit cleared to 0."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().strip().split()
    op = parts[0]
    n, i = int(parts[1]), int(parts[2])
    if op == "set":
        print(solve_set(n, i))
    else:
        print(solve_clear(n, i))

