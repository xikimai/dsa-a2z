"""
Solution for Challenge 2: Sieve of Eratosthenes
============================================
Chapter 7: Number Wizardry — Math for Programmers

APPROACH
--------
Classic sieve: boolean array, mark multiples starting from i*i.

TIME COMPLEXITY:  O(n log log n)
SPACE COMPLEXITY: O(n)
"""


def solve(n: int) -> list[int]:
    """Return all primes <= n using the Sieve of Eratosthenes."""
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    i = 2
    while i * i <= n:
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
        i += 1
    return [i for i in range(2, n + 1) if is_prime[i]]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    result = solve(n)
    print(" ".join(map(str, result)))
