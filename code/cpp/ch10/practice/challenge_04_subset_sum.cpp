/*
 * Challenge 4: Subset Sum
 * =========================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM:
 *   Given an array of non-negative integers and a target sum, determine
 *   if there exists a subset whose elements sum to target.
 *
 * EXAMPLES:
 *   solve({3,34,4,12,5,2}, 9)  -> true   (4+5 = 9)
 *   solve({3,34,4,12,5,2}, 30) -> false
 *   solve({}, 0)                -> true   (empty subset sums to 0)
 *   solve({1,2,3}, 6)          -> true   (1+2+3 = 6)
 *   solve({1,2,3}, 7)          -> false
 *
 * CONSTRAINTS:
 *   0 <= nums.size() <= 20
 *   0 <= nums[i] <= 100
 *   0 <= target <= 1000
 *
 * INSTRUCTIONS:
 *   Replace the body with your recursive solution.
 */

#include <iostream>
#include <vector>
using namespace std;

bool solve(vector<int> nums, int target) {
    // TODO: Replace this with your solution
    return false;
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
