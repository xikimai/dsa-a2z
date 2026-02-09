/*
 * Example 01: Knapsack Basics — Step-by-Step 0/1 Knapsack
 * =========================================================
 * Chapter 25: Dynamic Programming III — Subsequences & Knapsack
 *
 * Demonstrates 0/1 Knapsack: recursive and space-optimized.
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

// Recursive O(2^n)
int knapsackRecursive(vector<int>& w, vector<int>& v, int cap, int i) {
    if (i < 0 || cap <= 0) return 0;
    int skip = knapsackRecursive(w, v, cap, i - 1);
    int take = 0;
    if (w[i] <= cap)
        take = v[i] + knapsackRecursive(w, v, cap - w[i], i - 1);
    return max(skip, take);
}

// Space-optimized O(n * cap)
int knapsackOptimized(vector<int>& w, vector<int>& v, int cap) {
    vector<int> dp(cap + 1, 0);
    for (int i = 0; i < (int)w.size(); i++)
        for (int c = cap; c >= w[i]; c--)
            dp[c] = max(dp[c], dp[c - w[i]] + v[i]);
    return dp[cap];
}

int main() {
    vector<int> w = {1, 3, 4, 5};
    vector<int> v = {1, 4, 5, 7};
    int cap = 7;
    cout << "0/1 Knapsack" << endl;
    cout << "  Recursive: " << knapsackRecursive(w, v, cap, w.size() - 1) << endl;
    cout << "  Optimized: " << knapsackOptimized(w, v, cap) << endl;
    return 0;
}
