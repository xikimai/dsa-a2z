/*
 * Solution for Practice 6: Wildcard Matching
 * Chapter 25: Dynamic Programming III — Subsequences & Knapsack
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool solve(string s, string p) {
    int m = s.size(), n = p.size();
    vector<bool> prev(n + 1, false);
    prev[0] = true;
    for (int j = 1; j <= n; j++) {
        if (p[j-1] == '*') prev[j] = prev[j-1];
        else break;
    }
    for (int i = 1; i <= m; i++) {
        vector<bool> curr(n + 1, false);
        for (int j = 1; j <= n; j++) {
            if (p[j-1] == '*') curr[j] = curr[j-1] || prev[j];
            else if (p[j-1] == '?' || s[i-1] == p[j-1]) curr[j] = prev[j-1];
        }
        prev = curr;
    }
    return prev[n];
}

int main() { return 0; }
