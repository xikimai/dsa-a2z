"""
Solution for Practice 5: Longest Common Prefix
================================================
Chapter 5: Collections

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Compare characters column by column (i.e., position by position across
all strings). At each position, check if all strings have the same
character. Stop as soon as a mismatch is found or any string ends.

TIME COMPLEXITY:  O(S) where S = total number of characters across all strings
SPACE COMPLEXITY: O(1) — we only build the prefix
"""


def solve(strs: list[str]) -> str:
    """Return the longest common prefix of all strings."""
    if not strs:
        return ""

    # Use the first string as reference
    for i in range(len(strs[0])):
        char = strs[0][i]
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]

    return strs[0]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    strs = input().split()
    print(solve(strs))
