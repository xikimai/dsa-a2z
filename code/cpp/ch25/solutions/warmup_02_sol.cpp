/*
 * Solution for Warmup 2: Subset Sum
 * Chapter 25: Dynamic Programming III — Subsequences & Knapsack
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool solve(vector<int>& nums, int target) {
    vector<bool> dp(target + 1, false);
    dp[0] = true;
    for (int num : nums)
        for (int s = target; s >= num; s--)
            if (dp[s - num]) dp[s] = true;
    return dp[target];
}

int main() { return 0; }
