/*
 * Solution for Challenge 2: Rod Cutting
 * Chapter 25: Dynamic Programming III — Subsequences & Knapsack
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(vector<int>& prices) {
    int n = prices.size();
    vector<int> dp(n + 1, 0);
    for (int len = 1; len <= n; len++)
        for (int k = 1; k <= len; k++)
            dp[len] = max(dp[len], dp[len - k] + prices[k - 1]);
    return dp[n];
}

int main() { return 0; }
