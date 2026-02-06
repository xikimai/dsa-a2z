/*
 * Solution -- Practice 3: Sorted Squares
 * ========================================
 * Chapter 6: How Fast Is Your Code?
 *
 * APPROACH:
 *   Two-pointer technique. The largest squared value must come from
 *   either the leftmost (most negative) or rightmost (most positive)
 *   element. Compare absolute values from both ends, place the larger
 *   square at the back of the result, and move that pointer inward.
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(n) for the result array
 */

#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int>& nums) {
    int n = (int)nums.size();
    if (n == 0) return {};

    vector<int> result(n);
    int left = 0;
    int right = n - 1;
    int pos = n - 1;  // Fill from the back

    while (left <= right) {
        int left_sq = nums[left] * nums[left];
        int right_sq = nums[right] * nums[right];
        if (left_sq > right_sq) {
            result[pos] = left_sq;
            left++;
        } else {
            result[pos] = right_sq;
            right--;
        }
        pos--;
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
