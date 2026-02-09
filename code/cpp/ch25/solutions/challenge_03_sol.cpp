/*
 * Solution for Challenge 3: Target Sum
 * Chapter 25: Dynamic Programming III — Subsequences & Knapsack
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

int solve(vector<int>& nums, int target) {
    int total = accumulate(nums.begin(), nums.end(), 0);
    if ((total + target) % 2 != 0 || total + target < 0) return 0;
    int p = (total + target) / 2;
    if (p < 0) return 0;
    vector<int> dp(p + 1, 0);
    dp[0] = 1;
    for (int num : nums)
        for (int s = p; s >= num; s--)
            dp[s] += dp[s - num];
    return dp[p];
}

int main() { return 0; }
