/*
 * Practice 4: Sort by Frequency
 * ==============================
 * Chapter 5: Collections
 *
 * PROBLEM:
 *   Sort a vector of integers by frequency (most frequent first).
 *   If two elements have the same frequency, the smaller element
 *   comes first.
 *
 * EXAMPLES:
 *   solve({2, 3, 1, 3, 2}) -> {2, 2, 3, 3, 1}
 *   solve({1})              -> {1}
 *   solve({5, 5, 4, 4, 3}) -> {4, 4, 5, 5, 3}
 *
 * CONSTRAINTS:
 *   - 1 <= nums.size() <= 10^5
 */

#include <iostream>
#include <vector>
using namespace std;

/**
 * Returns nums sorted by frequency (desc), ties broken by value (asc).
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
