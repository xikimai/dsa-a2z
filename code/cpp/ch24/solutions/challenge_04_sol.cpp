/*
 * Solution for Challenge 4: Cherry Pickup I (3D DP)
 * Chapter 24: Dynamic Programming II — Grids and Paths
 */

#include <algorithm>
#include <climits>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& grid) {
    int n = grid.size();
    if (n == 0 || grid[0][0] == -1 || grid[n-1][n-1] == -1) return 0;
    const int NEG = INT_MIN / 2;
    vector<vector<int>> dp(n, vector<int>(n, NEG));
    dp[0][0] = grid[0][0];
    int maxT = 2 * (n - 1);
    for (int t = 1; t <= maxT; t++) {
        vector<vector<int>> newDp(n, vector<int>(n, NEG));
        int rLo = max(0, t - (n-1));
        int rHi = min(n-1, t);
        for (int r1 = rLo; r1 <= rHi; r1++) {
            int c1 = t - r1;
            if (c1 < 0 || c1 >= n || grid[r1][c1] == -1) continue;
            for (int r2 = rLo; r2 <= rHi; r2++) {
                int c2 = t - r2;
                if (c2 < 0 || c2 >= n || grid[r2][c2] == -1) continue;
                int best = NEG;
                for (int pr1 : {r1, r1-1})
                    for (int pr2 : {r2, r2-1})
                        if (pr1>=0 && pr2>=0 && pr1<n && pr2<n)
                            best = max(best, dp[pr1][pr2]);
                if (best == NEG) continue;
                int cherries = grid[r1][c1];
                if (r1 != r2) cherries += grid[r2][c2];
                newDp[r1][r2] = best + cherries;
            }
        }
        dp = newDp;
    }
    return max(0, dp[n-1][n-1]);
}

int main() { return 0; }
