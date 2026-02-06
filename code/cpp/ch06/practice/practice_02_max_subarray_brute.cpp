/*
 * Practice 2: Max Subarray Sum (Brute Force)
 * ==========================================
 * Chapter 6: How Fast Is Your Code?
 *
 * PROBLEM:
 *   Given a vector of integers, find the contiguous subarray with the
 *   largest sum and return that sum.  Use the O(n^2) brute force
 *   approach (check all subarrays).  Return 0 for an empty array.
 *
 * EXAMPLES:
 *   solve({-2, 1, -3, 4, -1, 2, 1, -5, 4}) -> 6   (subarray [4,-1,2,1])
 *   solve({1})                              -> 1
 *   solve({-1, -2, -3})                     -> -1
 *   solve({})                               -> 0
 *
 * CONSTRAINTS:
 *   - 0 <= nums.size() <= 10^4
 *   - -10^4 <= nums[i] <= 10^4
 */

#include <iostream>
#include <vector>
using namespace std;

/**
 * Returns the maximum subarray sum using O(n^2) brute force.
 */
int solve(vector<int>& nums) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    cout << solve(nums) << endl;
    return 0;
}
