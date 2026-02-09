/*
 * Solution for Challenge 4: Longest String Chain
 * Chapter 25: Dynamic Programming III — Subsequences & Knapsack
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

int solve(vector<string>& words) {
    sort(words.begin(), words.end(), [](const string& a, const string& b) {
        return a.size() < b.size();
    });
    unordered_map<string, int> dp;
    int best = 1;
    for (const string& word : words) {
        dp[word] = 1;
        for (int i = 0; i < (int)word.size(); i++) {
            string pred = word.substr(0, i) + word.substr(i + 1);
            if (dp.count(pred))
                dp[word] = max(dp[word], dp[pred] + 1);
        }
        best = max(best, dp[word]);
    }
    return best;
}

int main() { return 0; }
