/*
 * Solution for Challenge 2: Number of Ways to Wear Hats
 * Chapter 31: Advanced DP — Bitmask, Interval, Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1e9 + 7;

int solve(int n, vector<vector<int>>& hats) {
    vector<vector<int>> hatToPeople(41);
    for (int person = 0; person < n; person++)
        for (int hat : hats[person])
            hatToPeople[hat].push_back(person);

    int full = (1 << n) - 1;
    vector<long long> dp(1 << n, 0);
    dp[0] = 1;

    for (int hat = 1; hat <= 40; hat++) {
        vector<long long> newDp(dp);
        for (int mask = 0; mask <= full; mask++) {
            if (dp[mask] == 0) continue;
            for (int person : hatToPeople[hat]) {
                if (mask & (1 << person)) continue;
                int nm = mask | (1 << person);
                newDp[nm] = (newDp[nm] + dp[mask]) % MOD;
            }
        }
        dp = newDp;
    }

    return (int)dp[full];
}

int main() { return 0; }
