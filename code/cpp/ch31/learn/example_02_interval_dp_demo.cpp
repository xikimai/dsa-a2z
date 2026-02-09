/*
 * Example 02: Interval DP Demo — MCM & Burst Balloons
 * Chapter 31: Advanced DP — Bitmask, Interval, Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

int mcm(vector<int>& dims) {
    int n = dims.size() - 1;
    if (n <= 1) return 0;
    vector<vector<int>> dp(n, vector<int>(n, 0));
    for (int len = 2; len <= n; len++)
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            dp[i][j] = INT_MAX;
            for (int k = i; k < j; k++)
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + dims[i]*dims[k+1]*dims[j+1]);
        }
    return dp[0][n - 1];
}

int burstBalloons(vector<int>& nums) {
    int n = nums.size() + 2;
    vector<int> vals(n);
    vals[0] = vals[n - 1] = 1;
    for (int i = 0; i < (int)nums.size(); i++) vals[i + 1] = nums[i];
    vector<vector<int>> dp(n, vector<int>(n, 0));
    for (int len = 1; len <= n - 2; len++)
        for (int left = 1; left < n - len; left++) {
            int right = left + len - 1;
            for (int k = left; k <= right; k++) {
                int coins = vals[left-1]*vals[k]*vals[right+1] + dp[left][k-1] + dp[k+1][right];
                dp[left][right] = max(dp[left][right], coins);
            }
        }
    return dp[1][n - 2];
}

int main() {
    vector<int> dims = {10, 30, 5, 60};
    cout << "MCM [10,30,5,60] = " << mcm(dims) << endl;  // 4500

    vector<int> nums = {3, 1, 5, 8};
    cout << "Burst [3,1,5,8] = " << burstBalloons(nums) << endl;  // 167
    return 0;
}
