/*
 * Example 02: Space Optimization — Reducing 2D DP to 1D
 * Chapter 24: Dynamic Programming II — Grids and Paths
 *
 * Demonstrates: unique paths with obstacles, maximal square, count squares
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

int uniquePathsObstacles(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    if (grid[0][0] == 1) return 0;
    vector<int> dp(n, 0);
    dp[0] = 1;
    for (int j = 1; j < n; j++) dp[j] = grid[0][j] == 0 ? dp[j - 1] : 0;
    for (int i = 1; i < m; i++) {
        dp[0] = grid[i][0] == 0 ? dp[0] : 0;
        for (int j = 1; j < n; j++)
            dp[j] = grid[i][j] == 1 ? 0 : dp[j] + dp[j - 1];
    }
    return dp[n - 1];
}

int maximalSquare(vector<vector<int>>& matrix) {
    int m = matrix.size(), n = matrix[0].size();
    vector<int> dp(n, 0);
    int maxSide = 0, prevDiag = 0;
    for (int i = 0; i < m; i++) {
        prevDiag = 0;
        for (int j = 0; j < n; j++) {
            int temp = dp[j];
            if (matrix[i][j] == 1) {
                dp[j] = (i == 0 || j == 0) ? 1 : min({dp[j], dp[j-1], prevDiag}) + 1;
                maxSide = max(maxSide, dp[j]);
            } else {
                dp[j] = 0;
            }
            prevDiag = temp;
        }
    }
    return maxSide * maxSide;
}

int main() {
    vector<vector<int>> grid = {{0,0,0},{0,1,0},{0,0,0}};
    cout << "Obstacles: " << uniquePathsObstacles(grid) << endl;
    vector<vector<int>> matrix = {{1,0,1,0,0},{1,0,1,1,1},{1,1,1,1,1},{1,0,0,1,0}};
    cout << "Maximal Square: " << maximalSquare(matrix) << endl;
    return 0;
}
