"""
Solution for Warmup 3: Mystery Complexity
============================================
Chapter 6: How Fast Is Your Code?

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
1. Check if all counts are the same -> O(1).
2. For consecutive pairs where n roughly doubles, compute the ratio
   counts[i+1] / counts[i].
3. Average the ratios:
   - ratio ~ 1 (and count differences ~ 1) -> O(log n)
   - ratio ~ 2 -> O(n)
   - ratio ~ 4 -> O(n^2)

TIME COMPLEXITY:  O(k) where k is the number of data points
SPACE COMPLEXITY: O(1)
"""


def solve(n_values: list[int], counts: list[int]) -> str:
    """Classify the growth rate from observed (n, count) data points."""
    # Check O(1): all counts the same
    if len(set(counts)) == 1:
        return "O(1)"

    # Compute differences between consecutive counts
    diffs = []
    for i in range(len(n_values) - 1):
        diffs.append(counts[i + 1] - counts[i])

    # O(log n): when n doubles, count increases by a roughly constant
    # small amount (typically 1).  Check if all diffs are similar.
    avg_diff = sum(diffs) / len(diffs)
    if all(abs(d - avg_diff) <= 1 for d in diffs) and avg_diff <= 2:
        return "O(log n)"

    # Use ratios for the remaining cases (need non-zero counts)
    ratios = []
    for i in range(len(n_values) - 1):
        if counts[i] != 0:
            ratios.append(counts[i + 1] / counts[i])

    if ratios:
        avg_ratio = sum(ratios) / len(ratios)
    else:
        avg_ratio = 0

    # O(n): count doubles when n doubles -> ratio ~ 2
    # O(n^2): count quadruples when n doubles -> ratio ~ 4
    if avg_ratio < 3:
        return "O(n)"
    else:
        return "O(n^2)"


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n_values = list(map(int, input().split()))
    counts = list(map(int, input().split()))
    print(solve(n_values, counts))
