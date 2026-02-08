/*
 * Solution for Warmup 4: House Robber
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
    int n = nums.size();
    if (n == 0) return 0;
    if (n == 1) return nums[0];
    int prev2 = nums[0], prev1 = max(nums[0], nums[1]);
    for (int i = 2; i < n; i++) { int c = max(prev1, prev2 + nums[i]); prev2 = prev1; prev1 = c; }
    return prev1;
}

int main() {
    return 0;
}
