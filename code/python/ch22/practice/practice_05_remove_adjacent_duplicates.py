"""
Practice 5: Remove All Adjacent Duplicates in String
========================================================
Chapter 22: Stacks & Queues — Order Matters

PROBLEM
-------
Given a string s, repeatedly remove pairs of adjacent, equal characters
until no more removals can be made. Return the final string.

CONSTRAINTS
-----------
- 1 <= len(s) <= 10^5
- s consists of lowercase English letters only

EXAMPLES
--------
Input: "abbaca"
Output: "ca"

Input: "azxxzy"
Output: "ay"

HINT
----
Use a stack. If the current character matches the top, pop; otherwise push.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(s: str) -> str:
    """Remove all adjacent duplicates and return the result."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input().strip()
    print(solve(s))
