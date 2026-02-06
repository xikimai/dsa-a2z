"""
Solution for Challenge 03: Collatz Sequence
============================================
Chapter 3: Decisions and Loops

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Start with n, add it to the list, then repeatedly apply the rules:
  - Even: divide by 2
  - Odd: multiply by 3 and add 1
Continue until n becomes 1.

The Collatz conjecture says this always terminates, but nobody has
proven it! It's one of the most famous unsolved problems in math.

TIME COMPLEXITY:  O(?) — unknown! No proven bound on sequence length.
                  For practical inputs (n <= 10^6), it always terminates quickly.
SPACE COMPLEXITY: O(k) — where k is the length of the sequence
"""


def solve(n: int) -> list[int]:
    """Return the Collatz sequence starting from n until reaching 1."""
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
