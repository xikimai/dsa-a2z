/*
 * Solution for Practice 4: Cherry Pickup II
 * Chapter 24: Dynamic Programming II — Grids and Paths
 */

#include <algorithm>
#include <climits>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    vector<vector<int>> dp(n, vector<int>(n, -1));
    for (int c1 = 0; c1 < n; c1++)
        for (int c2 = 0; c2 < n; c2++)
            dp[c1][c2] = grid[m-1][c1] + (c1 != c2 ? grid[m-1][c2] : 0);
    for (int i = m-2; i >= 0; i--) {
        vector<vector<int>> newDp(n, vector<int>(n, -1));
        for (int c1 = 0; c1 < n; c1++)
            for (int c2 = 0; c2 < n; c2++) {
                int best = -1;
                for (int d1 = -1; d1 <= 1; d1++)
                    for (int d2 = -1; d2 <= 1; d2++) {
                        int nc1 = c1+d1, nc2 = c2+d2;
                        if (nc1>=0&&nc1<n&&nc2>=0&&nc2<n&&dp[nc1][nc2]!=-1)
                            best = max(best, dp[nc1][nc2]);
                    }
                if (best == -1) continue;
                int val = grid[i][c1] + (c1!=c2 ? grid[i][c2] : 0);
                newDp[c1][c2] = val + best;
            }
        dp = newDp;
    }
    return dp[0][n-1] != -1 ? dp[0][n-1] : 0;
}

int main() { return 0; }
