/*
 * Solution for Challenge 1: Dungeon Game
 * Chapter 24: Dynamic Programming II — Grids and Paths
 */

#include <algorithm>
#include <climits>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& dungeon) {
    int m = dungeon.size(), n = dungeon[0].size();
    vector<int> dp(n + 1, INT_MAX);
    dp[n - 1] = 1;
    for (int i = m - 1; i >= 0; i--) {
        vector<int> newDp(n + 1, INT_MAX);
        for (int j = n - 1; j >= 0; j--) {
            int minNext = min(dp[j], newDp[j + 1]);
            newDp[j] = max(1, minNext - dungeon[i][j]);
        }
        dp = newDp;
    }
    return dp[0];
}

int main() { return 0; }
