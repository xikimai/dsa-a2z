"""
Solution for Practice 1: All Divisors (Sorted)
============================================
Chapter 7: Number Wizardry — Math for Programmers

APPROACH
--------
Check all i from 1 to √n. If i divides n, add both i and n//i.
Handle perfect squares carefully (don't add √n twice).
Sort the result.

TIME COMPLEXITY:  O(√n)
SPACE COMPLEXITY: O(√n) for the divisor list
"""


def solve(n: int) -> list[int]:
    """Return a sorted list of all divisors of n."""
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    divisors.sort()
    return divisors


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    result = solve(n)
    print(" ".join(map(str, result)))
