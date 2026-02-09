"""
Solution for Practice 2: Accounts Merge
=========================================
Chapter 29: Union-Find & Minimum Spanning Trees

APPROACH
--------
Map each email to an integer index. Union all emails within the same account.
Then group emails by root, sort, and prepend the account name.

TIME COMPLEXITY:  O(N * alpha(N) + N log N) where N = total emails
SPACE COMPLEXITY: O(N)
"""

from collections import defaultdict


def solve(accounts: list[list[str]]) -> list[list[str]]:
    """Return merged accounts, each sorted by email, accounts sorted by first email."""
    parent = {}
    rank = {}
    email_to_name = {}

    def find(x):
        if x not in parent:
            parent[x] = x
            rank[x] = 0
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1

    # Union all emails within the same account
    for account in accounts:
        name = account[0]
        first_email = account[1]
        for email in account[1:]:
            email_to_name[email] = name
            union(first_email, email)

    # Group emails by root
    groups = defaultdict(set)
    for email in email_to_name:
        root = find(email)
        groups[root].add(email)

    # Build result
    result = []
    for root, emails in groups.items():
        name = email_to_name[root]
        result.append([name] + sorted(emails))

    # Sort accounts by first email
    result.sort(key=lambda acc: acc[1])
    return result


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
