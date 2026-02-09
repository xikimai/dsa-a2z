/*
 * Solution for Warmup 4: Coin Change II (Count Ways)
 * Chapter 25: Dynamic Programming III — Subsequences & Knapsack
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(vector<int>& coins, int amount) {
    vector<int> dp(amount + 1, 0);
    dp[0] = 1;
    for (int coin : coins)
        for (int a = coin; a <= amount; a++)
            dp[a] += dp[a - coin];
    return dp[amount];
}

int main() { return 0; }
