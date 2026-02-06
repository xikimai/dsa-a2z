"""
Challenge 2: Group Anagrams
==============================
Chapter 5: Collections

PROBLEM
-------
Given a list of strings, group the anagrams together. An anagram is a
word formed by rearranging the letters of another word.

Return the groups as a list of lists. Each inner group should be sorted
alphabetically, and the outer list should be sorted by the first element
of each group.

INPUT FORMAT
------------
A single line of space-separated strings.

OUTPUT FORMAT
-------------
Groups on separate lines, each group as space-separated strings.

CONSTRAINTS
-----------
- 1 <= len(strs) <= 10^4
- 0 <= len(strs[i]) <= 100
- strs[i] contains only lowercase English letters

EXAMPLES
--------
Input:  eat tea tan ate nat bat
Output:
ate eat tea
bat
nat tan

Input:  a
Output:
a

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(strs: list[str]) -> list[list[str]]:
    """Group anagrams together. Inner sorted, outer sorted by first element."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    strs = input().split()
    groups = solve(strs)
    for group in groups:
        print(" ".join(group))
