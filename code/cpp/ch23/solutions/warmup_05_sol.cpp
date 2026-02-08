/*
 * Solution for Warmup 5: Maximum Subarray (Kadane's)
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
    int cur = nums[0], best = nums[0];
    for (int i = 1; i < (int)nums.size(); i++) {
        cur = max(cur + nums[i], nums[i]);
        best = max(best, cur);
    }
    return best;
}

int main() {
    return 0;
}
