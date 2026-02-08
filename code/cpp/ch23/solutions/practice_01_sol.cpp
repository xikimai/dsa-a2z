/*
 * Solution for Practice 1: Frog Jump with K Steps
 * Chapter 23: Dynamic Programming I — The Foundation
 */

#include <algorithm>
#include <climits>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(vector<int> costs, int k) {
    int n = costs.size();
    if (n <= 1) return n == 1 ? costs[0] : 0;
    vector<int> dp(n, INT_MAX);
    dp[0] = costs[0];
    for (int i = 1; i < n; i++) {
        for (int j = 1; j <= min(k, i); j++) dp[i] = min(dp[i], dp[i-j]);
        dp[i] += costs[i];
    }
    return dp[n-1];
}

int main() {
    return 0;
}
