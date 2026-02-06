/*
 * Practice 1: Contains Duplicate
 * ==============================
 * Chapter 6: How Fast Is Your Code?
 *
 * PROBLEM:
 *   Given a vector of integers, return true if any value appears at
 *   least twice, and false if every element is distinct.
 *
 * EXAMPLES:
 *   solve({1, 2, 3, 1}) -> true
 *   solve({1, 2, 3, 4}) -> false
 *   solve({})           -> false
 *
 * CONSTRAINTS:
 *   - 0 <= nums.size() <= 10^5
 *   - Elements can be any integer
 *
 * HINT: Use an unordered_set for O(n) time.
 */

#include <iostream>
#include <vector>
using namespace std;

/**
 * Returns true if any element appears more than once.
 */
bool solve(vector<int>& nums) {
    // TODO: Replace this with your solution
    return false;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    cout << (solve(nums) ? "true" : "false") << endl;
    return 0;
}
