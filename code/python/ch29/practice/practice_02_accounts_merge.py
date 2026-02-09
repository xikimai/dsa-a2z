"""
Practice 2: Accounts Merge
==========================
Chapter 29: Union-Find & Minimum Spanning Trees

PROBLEM
-------
Return merged accounts, each sorted by email, accounts sorted by first email.

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Map each email to an integer index. Union all emails within the same account. Then group emails by root, sort, and prepend the account name.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from collections import defaultdict


def solve(accounts: list[list[str]]) -> list[list[str]]:
    """Return merged accounts, each sorted by email, accounts sorted by first email."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip().split("\n")
    idx = 0
    n = int(data[idx]); idx += 1
    accounts = []
    for _ in range(n):
        parts = data[idx].split(); idx += 1
        accounts.append(parts)
    result = solve(accounts)
    for acc in result:
        print(" ".join(acc))
