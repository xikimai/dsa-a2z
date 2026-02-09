"""
Example 02: String DP Basics — LCS with Table Visualization
============================================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

This example demonstrates DP on strings through the Longest Common
Subsequence (LCS) problem. We show:
  - The 2D DP approach with table visualization
  - How to reconstruct the actual LCS (not just its length)
  - Edit Distance as a close relative of LCS
"""


# ── LCS: Tabulation with Table Print ────────────────────────────

def lcs_with_table(text1, text2):
    """Compute LCS length and print the DP table."""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Print table
    print(f"\n  LCS Table for '{text1}' and '{text2}':")
    print(f"{'':>6}", end="")
    print(f"{'_':>4}", end="")
    for ch in text2:
        print(f"{ch:>4}", end="")
    print()
    for i in range(m + 1):
        label = "_" if i == 0 else text1[i - 1]
        print(f"  {label:>3}", end="  ")
        for j in range(n + 1):
            print(f"{dp[i][j]:>3}", end=" ")
        print()

    return dp[m][n]


# ── LCS: Reconstruct the Actual Subsequence ─────────────────────

def lcs_reconstruct(text1, text2):
    """Return the actual LCS string (not just length)."""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find the LCS
    i, j = m, n
    result = []
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            result.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(result))


# ── Edit Distance ────────────────────────────────────────────────

def edit_distance(word1, word2):
    """Min operations (insert/delete/replace) to convert word1 to word2."""
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases: transforming to/from empty string
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # no operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # delete from word1
                    dp[i][j - 1],      # insert into word1
                    dp[i - 1][j - 1],  # replace in word1
                )
    return dp[m][n]


# ── Demo ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("LONGEST COMMON SUBSEQUENCE (LCS)")
    print("=" * 60)

    length = lcs_with_table("abcde", "ace")
    lcs = lcs_reconstruct("abcde", "ace")
    print(f"  LCS length = {length}, LCS = '{lcs}'")

    length2 = lcs_with_table("oxcpqrsvwf", "shmtulqrypy")
    lcs2 = lcs_reconstruct("oxcpqrsvwf", "shmtulqrypy")
    print(f"  LCS length = {length2}, LCS = '{lcs2}'")

    print("\n" + "=" * 60)
    print("EDIT DISTANCE")
    print("=" * 60)

    cases = [
        ("horse", "ros", 3),
        ("intention", "execution", 5),
        ("", "abc", 3),
    ]
    for w1, w2, expected in cases:
        result = edit_distance(w1, w2)
        assert result == expected
        print(f"  '{w1}' -> '{w2}': {result} operations")

    print("\n  LCS and Edit Distance are closely related!")
    print("  Edit Distance('abc', 'axc') = 1 (replace b->x)")
    print("  LCS('abc', 'axc') = 'ac' (length 2)")
    print("  Relationship: edit_dist >= len(s1) + len(s2) - 2 * LCS_length")
