/*
 * Warmup 1: Second Largest
 * ========================
 * Chapter 5: Collections
 *
 * PROBLEM:
 *   Given a vector of integers, return the second largest element.
 *   If there is no second largest (all elements are the same or
 *   the vector has fewer than 2 elements), return -1.
 *
 * EXAMPLES:
 *   solve({3, 1, 4, 1, 5}) -> 4
 *   solve({7, 7, 7})       -> -1
 *   solve({1, 2})          -> 1
 *   solve({10})            -> -1
 *
 * CONSTRAINTS:
 *   - 1 <= nums.size() <= 10^5
 *   - Elements can be any integer
 */

#include <iostream>
#include <vector>
using namespace std;

/**
 * Returns the second largest element, or -1 if none exists.
 */
int solve(vector<int>& nums) {
    // TODO: Replace this with your solution
    return -1;
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
