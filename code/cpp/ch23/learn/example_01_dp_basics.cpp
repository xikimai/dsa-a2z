/*
 * Example 01: DP Basics — The Four Stages of Climbing Stairs
 * ===========================================================
 * Chapter 23: Dynamic Programming I — The Foundation
 *
 * Demonstrates: recursion -> memo -> tabulation -> space-optimized
 */

#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

// Stage 1: Pure Recursion O(2^n)
int climbRecursive(int n) {
    if (n <= 1) return 1;
    return climbRecursive(n - 1) + climbRecursive(n - 2);
}

// Stage 2: Memoization O(n)
int climbMemo(int n, unordered_map<int, int>& memo) {
    if (n <= 1) return 1;
    if (memo.count(n)) return memo[n];
    return memo[n] = climbMemo(n - 1, memo) + climbMemo(n - 2, memo);
}

// Stage 3: Tabulation O(n) time, O(n) space
int climbTabulation(int n) {
    if (n <= 1) return 1;
    vector<int> dp(n + 1);
    dp[0] = 1; dp[1] = 1;
    for (int i = 2; i <= n; i++) dp[i] = dp[i - 1] + dp[i - 2];
    return dp[n];
}

// Stage 4: Space-Optimized O(n) time, O(1) space
int climbOptimized(int n) {
    if (n <= 1) return 1;
    int prev2 = 1, prev1 = 1;
    for (int i = 2; i <= n; i++) {
        int current = prev1 + prev2;
        prev2 = prev1;
        prev1 = current;
    }
    return prev1;
}

// House Robber
int houseRobber(vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return 0;
    if (n == 1) return nums[0];
    int prev2 = nums[0], prev1 = max(nums[0], nums[1]);
    for (int i = 2; i < n; i++) {
        int c = max(prev1, prev2 + nums[i]);
        prev2 = prev1; prev1 = c;
    }
    return prev1;
}

// Kadane's
int maxSubarray(vector<int>& nums) {
    int cur = nums[0], best = nums[0];
    for (int i = 1; i < (int)nums.size(); i++) {
        cur = max(cur + nums[i], nums[i]);
        best = max(best, cur);
    }
    return best;
}

int main() {
    cout << "Climbing Stairs — Four Stages" << endl;
    for (int n : {1, 2, 3, 5, 10}) {
        cout << "  n=" << n << ": " << climbOptimized(n) << " ways" << endl;
    }

    cout << "\nHouse Robber" << endl;
    vector<int> h1 = {1, 2, 3, 1};
    vector<int> h2 = {2, 7, 9, 3, 1};
    cout << "  [1,2,3,1] -> " << houseRobber(h1) << endl;
    cout << "  [2,7,9,3,1] -> " << houseRobber(h2) << endl;

    cout << "\nKadane's Algorithm" << endl;
    vector<int> k = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout << "  [-2,1,-3,4,-1,2,1,-5,4] -> " << maxSubarray(k) << endl;

    return 0;
}
