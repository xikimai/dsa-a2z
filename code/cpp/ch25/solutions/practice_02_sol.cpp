/*
 * Solution for Practice 2: Unbounded Knapsack
 * Chapter 25: Dynamic Programming III — Subsequences & Knapsack
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(vector<int>& weights, vector<int>& values, int capacity) {
    vector<int> dp(capacity + 1, 0);
    for (int i = 0; i < (int)weights.size(); i++)
        for (int w = weights[i]; w <= capacity; w++)
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i]);
    return dp[capacity];
}

int main() { return 0; }
