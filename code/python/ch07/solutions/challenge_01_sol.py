"""
Solution for Challenge 1: GCD Three Ways
============================================
Chapter 7: Number Wizardry — Math for Programmers

APPROACH
--------
Three algorithms with different performance:
  1. Subtraction: O(max(a,b)) — replace larger with difference
  2. Euclidean:   O(log(min(a,b))) — replace larger with remainder
  3. Extended:    O(log(min(a,b))) — also finds x,y where ax+by=gcd

TIME COMPLEXITY:  O(log(min(a,b))) for Euclidean/Extended
SPACE COMPLEXITY: O(log(min(a,b))) for Extended (recursion stack), O(1) for others
"""


def solve_subtract(a: int, b: int) -> int:
    """GCD by repeated subtraction. O(max(a,b))."""
    if a == 0:
        return b
    if b == 0:
        return a
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def solve_euclidean(a: int, b: int) -> int:
    """GCD by Euclidean algorithm. O(log(min(a,b)))."""
    while b != 0:
        a, b = b, a % b
    return a


def solve_extended(a: int, b: int) -> list[int]:
    """Extended Euclidean: returns [gcd, x, y] where a*x + b*y = gcd."""
    if b == 0:
        return [a, 1, 0]
    gcd, x1, y1 = solve_extended(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return [gcd, x, y]


def solve(a: int, b: int) -> int:
    """Default GCD — uses Euclidean algorithm."""
    return solve_euclidean(a, b)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    a, b = map(int, input().split())
    print(solve(a, b))
