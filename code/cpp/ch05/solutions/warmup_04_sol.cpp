/*
 * Solution -- Warmup 4: Remove Duplicates
 * =========================================
 * Chapter 5: Collections
 *
 * APPROACH:
 *   Two-pointer technique on a sorted array. Use a write pointer that
 *   advances only when we see a new value (different from the previous).
 *   The read pointer scans every element.
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(1) extra (output vector not counted)
 */

#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int>& nums) {
    if (nums.empty()) return {};

    vector<int> result;
    result.push_back(nums[0]);
    for (int i = 1; i < (int)nums.size(); i++) {
        if (nums[i] != nums[i - 1]) {
            result.push_back(nums[i]);
        }
    }
    return result;
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
