/*
 * Solution for Challenge 4: Palindrome Partitioning II
 * Chapter 31: Advanced DP — Bitmask, Interval, Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(string& s) {
    int n = s.size();
    if (n <= 1) return 0;

    vector<vector<bool>> isPal(n, vector<bool>(n, false));
    for (int i = 0; i < n; i++) isPal[i][i] = true;
    for (int i = 0; i < n - 1; i++) isPal[i][i + 1] = (s[i] == s[i + 1]);
    for (int len = 3; len <= n; len++)
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            isPal[i][j] = (s[i] == s[j]) && isPal[i + 1][j - 1];
        }

    vector<int> dp(n);
    for (int i = 0; i < n; i++) {
        if (isPal[0][i]) {
            dp[i] = 0;
        } else {
            dp[i] = i;
            for (int j = 1; j <= i; j++)
                if (isPal[j][i])
                    dp[i] = min(dp[i], dp[j - 1] + 1);
        }
    }

    return dp[n - 1];
}

int main() { return 0; }
