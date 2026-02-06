"""
Practice 5: Longest Common Prefix
===================================
Chapter 5: Collections

PROBLEM
-------
Given a list of strings, find the longest common prefix string
amongst them. If there is no common prefix, return an empty string "".

INPUT FORMAT
------------
A single line of space-separated strings.

OUTPUT FORMAT
-------------
The longest common prefix string (could be empty).

CONSTRAINTS
-----------
- 1 <= len(strs) <= 200
- 0 <= len(strs[i]) <= 200
- strs[i] contains only lowercase English letters

EXAMPLES
--------
Input:  flower flow flight
Output: fl

Input:  dog racecar car
Output: (empty line)

Input:  abc
Output: abc

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(strs: list[str]) -> str:
    """Return the longest common prefix of all strings."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    strs = input().split()
    print(solve(strs))
