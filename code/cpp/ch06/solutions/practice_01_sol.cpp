/*
 * Solution -- Practice 1: Contains Duplicate
 * ============================================
 * Chapter 6: How Fast Is Your Code?
 *
 * APPROACH:
 *   Use an unordered_set to track seen elements. For each element,
 *   check if it's already in the set. If yes, return true.
 *   If we finish without finding a duplicate, return false.
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(n)
 */

#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

bool solve(vector<int>& nums) {
    unordered_set<int> seen;
    for (int x : nums) {
        if (seen.count(x)) return true;
        seen.insert(x);
    }
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
