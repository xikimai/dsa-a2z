"""
Practice 1: Group Anagrams
==============================
Chapter 11: Hashing — The Secret Decoder Ring

PROBLEM
-------
Given a list of strings, group the anagrams together.
Return the groups sorted: each group sorted alphabetically,
and the outer list sorted by the first element of each group.

INPUT FORMAT
------------
A single line of space-separated strings.

OUTPUT FORMAT
-------------
A list of lists — each inner list is a group of anagrams.

CONSTRAINTS
-----------
- 0 <= len(strs) <= 10^4
- 0 <= len(strs[i]) <= 100
- strs[i] consists of lowercase English letters

EXAMPLES
--------
Input:
  eat tea tan ate nat bat
Output: [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]

Input:
  abc bca cab xyz zxy
Output: [["abc", "bca", "cab"], ["xyz", "zxy"]]

Input:
  (empty)
Output: []

HINT
----
Sort each string's characters to create a canonical key.
Use a dictionary to group strings with the same key.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(strs: list[str]) -> list[list[str]]:
    """Group strings by anagram equivalence."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        strs = line.split()
    else:
        strs = []
    print(solve(strs))
