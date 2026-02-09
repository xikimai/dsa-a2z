/*
 * Solution for Practice 3: Minimum Score Triangulation of Polygon
 * Chapter 31: Advanced DP — Bitmask, Interval, Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int>& values) {
    int n = values.size();
    if (n < 3) return 0;
    vector<vector<int>> dp(n, vector<int>(n, 0));

    for (int len = 3; len <= n; len++)
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            dp[i][j] = INT_MAX;
            for (int k = i + 1; k < j; k++) {
                int cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j];
                dp[i][j] = min(dp[i][j], cost);
            }
        }

    return dp[0][n - 1];
}

int main() { return 0; }
