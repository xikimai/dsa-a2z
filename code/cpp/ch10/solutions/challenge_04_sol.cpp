/*
 * Solution -- Challenge 4: Subset Sum
 * ======================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Helper with index and remaining target.
 *           At each element: include it (subtract from target) or exclude it.
 *           Base case: remaining == 0 means found; idx == n means exhausted.
 * TIME:  O(2^n)
 * SPACE: O(n) call stack
 */

#include <iostream>
#include <vector>
using namespace std;

bool helper(const vector<int>& nums, int idx, int remaining) {
    if (remaining == 0) return true;
    if (idx == (int)nums.size()) return false;
    // Include nums[idx]
    if (helper(nums, idx + 1, remaining - nums[idx])) return true;
    // Exclude nums[idx]
    return helper(nums, idx + 1, remaining);
}

bool solve(vector<int> nums, int target) {
    return helper(nums, 0, target);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    int target;
    cin >> target;
    cout << (solve(nums, target) ? "true" : "false") << endl;
    return 0;
}
