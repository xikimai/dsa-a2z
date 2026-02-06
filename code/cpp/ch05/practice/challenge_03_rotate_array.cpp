/*
 * Challenge 3: Rotate Array
 * =========================
 * Chapter 5: Collections
 *
 * PROBLEM:
 *   Rotate a vector to the right by k positions.
 *   Handle k larger than the vector size.
 *
 * EXAMPLES:
 *   solve({1, 2, 3, 4, 5, 6, 7}, 3) -> {5, 6, 7, 1, 2, 3, 4}
 *   solve({1, 2, 3}, 1)              -> {3, 1, 2}
 *   solve({1, 2, 3}, 5)              -> {2, 3, 1}  (5 % 3 = 2)
 *
 * CONSTRAINTS:
 *   - 0 <= nums.size() <= 10^5
 *   - 0 <= k <= 10^9
 */

#include <iostream>
#include <vector>
using namespace std;

/**
 * Rotates nums to the right by k positions.
 */
vector<int> solve(vector<int>& nums, int k) {
    // TODO: Replace this with your solution
    return nums;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    int k;
    cin >> k;
    vector<int> result = solve(nums, k);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
