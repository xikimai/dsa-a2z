/*
 * Solution for Practice 2: Burst Balloons
 * Chapter 31: Advanced DP — Bitmask, Interval, Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int>& nums) {
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

int main() { return 0; }
