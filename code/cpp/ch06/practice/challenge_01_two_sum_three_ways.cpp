/*
 * Challenge 1: Two Sum Three Ways
 * ================================
 * Chapter 6: How Fast Is Your Code?
 *
 * PROBLEM:
 *   Given a vector of integers and a target, return the indices of the
 *   two numbers that add up to target.  If no solution exists, return
 *   {-1, -1}.
 *
 *   Implement THREE approaches:
 *     1. solve_brute — O(n^2) check all pairs
 *     2. solve_sort  — O(n log n) sort + two pointers
 *     3. solve_hash  — O(n) hash map
 *   solve() calls solve_hash (the best one).
 *
 * EXAMPLES:
 *   solve({2, 7, 11, 15}, 9) -> {0, 1}
 *   solve({3, 3}, 6)         -> {0, 1}
 *   solve({1, 2, 3}, 10)     -> {-1, -1}
 *
 * CONSTRAINTS:
 *   - 2 <= nums.size() <= 10^5
 *   - Exactly one solution exists (or none, return {-1, -1})
 *   - Return indices in ascending order
 */

#include <iostream>
#include <vector>
using namespace std;

/**
 * Brute force: check every pair. O(n^2).
 */
vector<int> solve_brute(vector<int>& nums, int target) {
    // TODO: Replace this with your solution
    return {-1, -1};
}

/**
 * Sort + two pointers. O(n log n).
 */
vector<int> solve_sort(vector<int>& nums, int target) {
    // TODO: Replace this with your solution
    return {-1, -1};
}

/**
 * Hash map approach. O(n).
 */
vector<int> solve_hash(vector<int>& nums, int target) {
    // TODO: Replace this with your solution
    return {-1, -1};
}

/**
 * Default: calls the best approach.
 */
vector<int> solve(vector<int>& nums, int target) {
    return solve_hash(nums, target);
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
