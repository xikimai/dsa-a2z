/*
 * Solution for Challenge 5: Minimum Insertions for Palindrome
 * Chapter 25: Dynamic Programming III — Subsequences & Knapsack
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(string s) {
    int n = s.size();
    string t(s.rbegin(), s.rend());
    vector<int> prev(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        vector<int> curr(n + 1, 0);
        for (int j = 1; j <= n; j++) {
            if (s[i-1] == t[j-1]) curr[j] = prev[j-1] + 1;
            else curr[j] = max(prev[j], curr[j-1]);
        }
        prev = curr;
    }
    return n - prev[n];
}

int main() { return 0; }
