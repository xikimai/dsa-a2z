/*
 * Practice 4: Majority Element
 * ============================
 * Chapter 6: How Fast Is Your Code?
 *
 * PROBLEM:
 *   Given a vector of integers, return the majority element -- the
 *   element that appears more than n/2 times.  You may assume the
 *   majority element always exists.
 *
 *   Use Boyer-Moore Voting Algorithm for O(n) time, O(1) space.
 *
 * EXAMPLES:
 *   solve({3, 2, 3})             -> 3
 *   solve({2, 2, 1, 1, 1, 2, 2}) -> 2
 *   solve({1})                   -> 1
 *
 * CONSTRAINTS:
 *   - 1 <= nums.size() <= 10^5
 *   - The majority element is guaranteed to exist
 */

#include <iostream>
#include <vector>
using namespace std;

/**
 * Returns the majority element using Boyer-Moore Voting.
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
