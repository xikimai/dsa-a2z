/*
 * Practice 3: Two Sum
 * ====================
 * Chapter 5: Collections
 *
 * PROBLEM:
 *   Given a vector of integers and a target sum, return the indices
 *   of the two numbers that add up to the target. If no such pair
 *   exists, return {-1, -1}.
 *
 * EXAMPLES:
 *   solve({2, 7, 11, 15}, 9) -> {0, 1}
 *   solve({3, 3}, 6)         -> {0, 1}
 *   solve({1, 2, 3}, 10)     -> {-1, -1}
 *
 * CONSTRAINTS:
 *   - 2 <= nums.size() <= 10^4
 *   - Each input has at most one valid answer
 *   - You may not use the same element twice
 */

#include <iostream>
#include <vector>
using namespace std;

/**
 * Returns indices of two numbers that sum to target, or {-1, -1}.
 */
vector<int> solve(vector<int>& nums, int target) {
    // TODO: Replace this with your solution
    return {-1, -1};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    int target;
    cin >> target;
    vector<int> result = solve(nums, target);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}
