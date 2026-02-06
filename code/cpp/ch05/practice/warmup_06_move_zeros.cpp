/*
 * Warmup 6: Move Zeros
 * ====================
 * Chapter 5: Collections
 *
 * PROBLEM:
 *   Move all zeros in a vector to the end while maintaining the
 *   relative order of non-zero elements. Modify in place.
 *
 * EXAMPLES:
 *   solve({0, 1, 0, 3, 12}) -> {1, 3, 12, 0, 0}
 *   solve({1, 2, 3})        -> {1, 2, 3}
 *   solve({0, 0, 0})        -> {0, 0, 0}
 *
 * CONSTRAINTS:
 *   - 0 <= nums.size() <= 10^5
 */

#include <iostream>
#include <vector>
using namespace std;

/**
 * Moves zeros to the end in place, returns the modified vector.
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
