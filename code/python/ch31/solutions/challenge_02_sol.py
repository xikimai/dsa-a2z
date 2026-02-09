"""
Solution for Challenge 2: Number of Ways to Wear Hats
======================================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

APPROACH
--------
Bitmask DP on people (n <= 10, so 2^10 = 1024 states).
Iterate over hats 1..40. For each hat, either skip it or assign
it to one eligible person who hasn't been assigned yet.
dp[mask] = number of ways to assign hats such that exactly the
people in mask have been given a hat.

TIME COMPLEXITY:  O(40 * 2^n * n)
SPACE COMPLEXITY: O(2^n)
"""

MOD = 10**9 + 7


def solve(n: int, hats: list[list[int]]) -> int:
    """Return number of ways to assign distinct hats, mod 10^9+7."""
    # For each hat, which people can wear it
    hat_to_people = [[] for _ in range(41)]
    for person in range(n):
        for hat in hats[person]:
            hat_to_people[hat].append(person)

    full = (1 << n) - 1
    dp = [0] * (1 << n)
    dp[0] = 1  # no one has a hat yet

    for hat in range(1, 41):
        # Process in reverse to avoid using same hat twice
        new_dp = dp[:]
        for mask in range(full + 1):
            if dp[mask] == 0:
                continue
            for person in hat_to_people[hat]:
                if mask & (1 << person):
                    continue  # person already has a hat
                new_mask = mask | (1 << person)
                new_dp[new_mask] = (new_dp[new_mask] + dp[mask]) % MOD
        dp = new_dp

    return dp[full]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    hats = []
    for _ in range(n):
        cnt = int(tokens[idx]); idx += 1
        person_hats = []
        for _ in range(cnt):
            person_hats.append(int(tokens[idx])); idx += 1
        hats.append(person_hats)
    print(solve(n, hats))
