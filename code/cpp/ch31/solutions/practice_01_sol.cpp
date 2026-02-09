/*
 * Solution for Practice 1: Shortest Hamiltonian Path
 * Chapter 31: Advanced DP — Bitmask, Interval, Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

int solve(int n, vector<vector<int>>& dist) {
    int INF = INT_MAX / 2;
    int full = (1 << n) - 1;
    vector<vector<int>> dp(1 << n, vector<int>(n, INF));

    for (int i = 0; i < n; i++)
        dp[1 << i][i] = 0;

    for (int mask = 1; mask <= full; mask++)
        for (int u = 0; u < n; u++) {
            if (dp[mask][u] >= INF) continue;
            if (!(mask & (1 << u))) continue;
            for (int v = 0; v < n; v++) {
                if (mask & (1 << v)) continue;
                int nm = mask | (1 << v);
                dp[nm][v] = min(dp[nm][v], dp[mask][u] + dist[u][v]);
            }
        }

    int ans = INF;
    for (int u = 0; u < n; u++)
        ans = min(ans, dp[full][u]);
    return ans;
}

int main() { return 0; }
