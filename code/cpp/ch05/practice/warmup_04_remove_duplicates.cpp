/*
 * Warmup 4: Remove Duplicates
 * ============================
 * Chapter 5: Collections
 *
 * PROBLEM:
 *   Given a SORTED vector of integers, remove duplicates and return
 *   a new vector with only unique elements.
 *
 * EXAMPLES:
 *   solve({1, 1, 2})          -> {1, 2}
 *   solve({1, 1, 1, 2, 2, 3}) -> {1, 2, 3}
 *   solve({1})                -> {1}
 *
 * CONSTRAINTS:
 *   - 1 <= nums.size() <= 10^5
 *   - nums is sorted in non-decreasing order
 */

#include <iostream>
#include <vector>
using namespace std;

/**
 * Removes duplicates from a sorted vector, returns new vector.
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
