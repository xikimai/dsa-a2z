/*
 * Practice 3: Sorted Squares
 * ==========================
 * Chapter 6: How Fast Is Your Code?
 *
 * PROBLEM:
 *   Given a vector of integers sorted in non-decreasing order, return
 *   a vector of the squares of each number, also in non-decreasing order.
 *
 *   Use the two-pointer technique for O(n) time.
 *
 * EXAMPLES:
 *   solve({-4, -1, 0, 3, 10}) -> {0, 1, 9, 16, 100}
 *   solve({-3, -2, -1})       -> {1, 4, 9}
 *   solve({0, 1, 2, 3})       -> {0, 1, 4, 9}
 *   solve({})                 -> {}
 *
 * CONSTRAINTS:
 *   - 0 <= nums.size() <= 10^5
 *   - nums is sorted in non-decreasing order
 *   - -10^4 <= nums[i] <= 10^4
 */

#include <iostream>
#include <vector>
using namespace std;

/**
 * Returns sorted squares using the two-pointer O(n) approach.
 */
vector<int> solve(vector<int>& nums) {
    // TODO: Replace this with your solution
    return {};
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
