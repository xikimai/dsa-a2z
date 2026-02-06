"""
Solution for Warmup 06: Multiplication Table
============================================
Chapter 3: Decisions and Loops

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Loop from 1 to 10 and build each line using an f-string with the
format "i x n = result".

TIME COMPLEXITY:  O(1) — always exactly 10 iterations
SPACE COMPLEXITY: O(1) — the output list has a fixed size of 10
"""


def solve(n: int) -> list[str]:
    """Return n's multiplication table as a list of strings."""
    return [f"{i} x {n} = {i * n}" for i in range(1, 11)]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    for line in solve(n):
        print(line)
