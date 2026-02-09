/*
 * Solution for Practice 2: Minimum Falling Path Sum
 * Chapter 24: Dynamic Programming II — Grids and Paths
 */

#include <algorithm>
#include <climits>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& matrix) {
    int n = matrix.size();
    vector<int> dp = matrix[0];
    for (int i = 1; i < n; i++) {
        vector<int> newDp(n);
        for (int j = 0; j < n; j++) {
            int best = dp[j];
            if (j > 0) best = min(best, dp[j-1]);
            if (j < n-1) best = min(best, dp[j+1]);
            newDp[j] = matrix[i][j] + best;
        }
        dp = newDp;
    }
    return *min_element(dp.begin(), dp.end());
}

int main() { return 0; }
