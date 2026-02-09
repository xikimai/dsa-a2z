/*
 * Example 01: Grid DP Basics — From 1D to 2D
 * Chapter 24: Dynamic Programming II — Grids and Paths
 *
 * Demonstrates: unique paths, min path sum, triangle (space-optimized)
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

int uniquePaths(int m, int n) {
    vector<int> dp(n, 1);
    for (int i = 1; i < m; i++)
        for (int j = 1; j < n; j++)
            dp[j] += dp[j - 1];
    return dp[n - 1];
}

int minPathSum(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    vector<int> dp(n);
    dp[0] = grid[0][0];
    for (int j = 1; j < n; j++) dp[j] = dp[j - 1] + grid[0][j];
    for (int i = 1; i < m; i++) {
        dp[0] += grid[i][0];
        for (int j = 1; j < n; j++)
            dp[j] = min(dp[j], dp[j - 1]) + grid[i][j];
    }
    return dp[n - 1];
}

int triangleMinTotal(vector<vector<int>>& tri) {
    int n = tri.size();
    vector<int> dp = tri[n - 1];
    for (int i = n - 2; i >= 0; i--)
        for (int j = 0; j <= i; j++)
            dp[j] = tri[i][j] + min(dp[j], dp[j + 1]);
    return dp[0];
}

int main() {
    cout << "Unique Paths (3,7) = " << uniquePaths(3, 7) << endl;
    vector<vector<int>> grid = {{1,3,1},{1,5,1},{4,2,1}};
    cout << "Min Path Sum = " << minPathSum(grid) << endl;
    vector<vector<int>> tri = {{2},{3,4},{6,5,7},{4,1,8,3}};
    cout << "Triangle Min = " << triangleMinTotal(tri) << endl;
    return 0;
}
