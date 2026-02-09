"""
Solution for Practice 4: Repeated String Match
================================================
Chapter 32: String Algorithms — Beyond Brute Force

APPROACH
--------
The minimum number of repeats needed is at least ceil(len(b) / len(a)).
We try that many repeats and one more. If b is not found as a substring
in either case, return -1.

Why ceil(len(b)/len(a)) + 1 is enough:
- We need enough copies of a to cover all of b.
- b might start in the middle of one copy and end in the middle of another,
  so we need at most one extra copy beyond what covers b's length.

TIME COMPLEXITY:  O(n * m) where n = repeats * len(a), m = len(b)
SPACE COMPLEXITY: O(n)
"""


def solve(a: str, b: str) -> int:
    """Return minimum repeats of a so that b is a substring, or -1 if impossible."""
    if not a or not b:
        return -1 if b else 1

    # Minimum repeats to cover length of b
    repeats = -(-len(b) // len(a))  # ceiling division

    # Try repeats and repeats + 1
    repeated = a * repeats
    if b in repeated:
        return repeats

    repeated += a
    if b in repeated:
        return repeats + 1

    return -1


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    print(solve(data[0], data[1]))
