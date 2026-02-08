/*
 * Solution for Practice 2: House Robber II (Circular)
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
    if (n == 2) return max(nums[0], nums[1]);
    auto rob = [&](int lo, int hi) {
        int p2 = nums[lo], p1 = max(nums[lo], nums[lo+1]);
        for (int i = lo+2; i <= hi; i++) { int c = max(p1, p2+nums[i]); p2 = p1; p1 = c; }
        return p1;
    };
    return max(rob(0, n-2), rob(1, n-1));
}

int main() {
    return 0;
}
