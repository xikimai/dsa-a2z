/*
 * Solution for Practice 1: Partition Equal Subset Sum
 * Chapter 25: Dynamic Programming III — Subsequences & Knapsack
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

bool solve(vector<int>& nums) {
    int total = accumulate(nums.begin(), nums.end(), 0);
    if (total % 2 != 0) return false;
    int target = total / 2;
    vector<bool> dp(target + 1, false);
    dp[0] = true;
    for (int num : nums)
        for (int s = target; s >= num; s--)
            if (dp[s - num]) dp[s] = true;
    return dp[target];
}

int main() { return 0; }
