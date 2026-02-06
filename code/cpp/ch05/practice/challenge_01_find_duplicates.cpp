/*
 * Challenge 1: Find Duplicates (Multiple Approaches)
 * ===================================================
 * Chapter 5: Collections
 *
 * PROBLEM:
 *   Given a vector of integers, return a sorted vector of all elements
 *   that appear more than once.
 *
 * EXAMPLES:
 *   solve({4, 3, 2, 7, 8, 2, 3, 1}) -> {2, 3}
 *   solve({1, 2, 3})                 -> {}
 *   solve({1, 1, 1, 1})              -> {1}
 *
 * CONSTRAINTS:
 *   - 1 <= nums.size() <= 10^5
 *   - 1 <= nums[i] <= 10^5
 *
 * CHALLENGE: Implement THREE approaches:
 *   1. solve_brute — O(n^2) brute force
 *   2. solve_sort  — O(n log n) sort first
 *   3. solve_set   — O(n) using a set
 *   solve() calls solve_set (the best one).
 */

#include <iostream>
#include <vector>
using namespace std;

/**
 * Brute force: check every pair. O(n^2).
 */
vector<int> solve_brute(vector<int>& nums) {
    // TODO: Replace this with your solution
    return {};
}

/**
 * Sort first, then find adjacent duplicates. O(n log n).
 */
vector<int> solve_sort(vector<int>& nums) {
    // TODO: Replace this with your solution
    return {};
}

/**
 * Use a set to track seen elements. O(n).
 */
vector<int> solve_set(vector<int>& nums) {
    // TODO: Replace this with your solution
    return {};
}

/**
 * Default: calls the best approach.
 */
vector<int> solve(vector<int>& nums) {
    return solve_set(nums);
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
