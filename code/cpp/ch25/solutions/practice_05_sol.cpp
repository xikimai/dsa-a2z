/*
 * Solution for Practice 5: Distinct Subsequences
 * Chapter 25: Dynamic Programming III — Subsequences & Knapsack
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(string s, string t) {
    int m = s.size(), n = t.size();
    vector<int> dp(n + 1, 0);
    dp[0] = 1;
    for (int i = 1; i <= m; i++)
        for (int j = min(i, n); j >= 1; j--)
            if (s[i-1] == t[j-1]) dp[j] += dp[j-1];
    return dp[n];
}

int main() { return 0; }
