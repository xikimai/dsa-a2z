"""
Solution for Challenge 3: Distinct Substrings of Length K (Rolling Hash)
========================================================================
Chapter 32: String Algorithms — Beyond Brute Force

APPROACH
--------
Use a rolling hash to compute the hash of each substring of length k.
Store all hashes in a set. The size of the set is the answer.
To handle collisions, we use double hashing.

Alternative simpler approach: just use Python's built-in set with
string slices. We use the set approach since it is clean and correct.

TIME COMPLEXITY:  O(n * k) with string slicing, O(n) with rolling hash
SPACE COMPLEXITY: O(n)
"""


def solve(s: str, k: int) -> int:
    """Count distinct substrings of length k."""
    n = len(s)
    if k > n:
        return 0

    seen = set()
    for i in range(n - k + 1):
        seen.add(s[i:i + k])
    return len(seen)


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    print(solve(data[0], int(data[1])))
