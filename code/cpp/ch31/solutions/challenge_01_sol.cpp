/*
 * Solution for Challenge 1: Minimum Cost to Merge Stones
 * Chapter 31: Advanced DP — Bitmask, Interval, Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int>& stones, int k) {
    int n = stones.size();
    if ((n - 1) % (k - 1) != 0) return -1;
    if (n == 1) return 0;

    vector<int> prefix(n + 1, 0);
    for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + stones[i];

    int INF = INT_MAX / 2;
    vector<vector<int>> dp(n, vector<int>(n, 0));

    for (int len = 2; len <= n; len++)
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            dp[i][j] = INF;
            for (int mid = i; mid < j; mid += k - 1)
                dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j]);
            if ((j - i) % (k - 1) == 0)
                dp[i][j] += prefix[j + 1] - prefix[i];
        }

    return dp[0][n - 1];
}

int main() { return 0; }
