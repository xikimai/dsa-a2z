/*
 * Solution for Warmup 4: Triangle Minimum Total
 * Chapter 24: Dynamic Programming II — Grids and Paths
 */

#include <algorithm>
#include <climits>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& triangle) {
    int n = triangle.size();
    vector<int> dp = triangle[n - 1];
    for (int i = n - 2; i >= 0; i--)
        for (int j = 0; j <= i; j++)
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1]);
    return dp[0];
}

int main() { return 0; }
