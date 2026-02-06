/*
 * Warmup 2: Reverse List
 * ======================
 * Chapter 5: Collections
 *
 * PROBLEM:
 *   Reverse a vector of integers in place without using std::reverse.
 *   Return the reversed vector.
 *
 * EXAMPLES:
 *   solve({1, 2, 3, 4, 5}) -> {5, 4, 3, 2, 1}
 *   solve({1})              -> {1}
 *   solve({})               -> {}
 *
 * CONSTRAINTS:
 *   - 0 <= nums.size() <= 10^5
 */

#include <iostream>
#include <vector>
using namespace std;

/**
 * Reverses nums in place and returns it.
 * Do NOT use std::reverse.
 */
vector<int> solve(vector<int>& nums) {
    // TODO: Replace this with your solution
    return nums;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    vector<int> result = solve(nums);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
