/*
 * Solution — Warmup 5: Double List
 * =================================
 * Chapter 4: Functions
 *
 * APPROACH:
 *   Iterate through the vector by reference and multiply each element by 2.
 *   Because we take a reference (vector<int>&), the original vector is
 *   modified in place. We also return it for convenience.
 *
 * TIME COMPLEXITY:  O(n) where n = nums.size()
 * SPACE COMPLEXITY: O(1) — modifies in place, no extra space
 */

#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int>& nums) {
    for (int i = 0; i < (int)nums.size(); i++) {
        nums[i] *= 2;
    }
    return nums;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    vector<int> result = solve(nums);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
