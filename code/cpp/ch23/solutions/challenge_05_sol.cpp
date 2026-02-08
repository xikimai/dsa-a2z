/*
 * Solution for Challenge 5: Longest Increasing Subsequence
 * Chapter 23: Dynamic Programming I — The Foundation
 */

#include <algorithm>
#include <climits>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(vector<int> nums) {
    if (nums.empty()) return 0;
    int n = nums.size();
    vector<int> dp(n, 1);
    int best = 1;
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++)
            if (nums[j] < nums[i]) dp[i] = max(dp[i], dp[j]+1);
        best = max(best, dp[i]);
    }
    return best;
}

int main() {
    return 0;
}
