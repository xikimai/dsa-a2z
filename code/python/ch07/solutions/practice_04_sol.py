"""
Solution for Practice 4: Prime Factorization
============================================
Chapter 7: Number Wizardry — Math for Programmers

APPROACH
--------
Trial division: check each potential factor from 2 up to √n.
If i divides n, count how many times and add [i, count].
If n > 1 after the loop, n itself is a prime factor.

TIME COMPLEXITY:  O(√n)
SPACE COMPLEXITY: O(log n) for the factor list
"""


def solve(n: int) -> list[list[int]]:
    """Return prime factorization as [[prime, count], ...] sorted by prime."""
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            count = 0
            while n % d == 0:
                count += 1
                n //= d
            factors.append([d, count])
        d += 1
    if n > 1:
        factors.append([n, 1])
    return factors


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    result = solve(n)
    for prime, count in result:
        print(f"{prime}^{count}", end=" ")
    print()
