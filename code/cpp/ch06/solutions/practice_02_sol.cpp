/*
 * Solution -- Practice 2: Max Subarray Sum (Brute Force)
 * =======================================================
 * Chapter 6: How Fast Is Your Code?
 *
 * APPROACH:
 *   O(n^2) brute force: try all starting indices, accumulate the sum
 *   for each subarray extending to the right, and track the maximum.
 *   Return 0 for empty arrays.
 *
 * TIME COMPLEXITY:  O(n^2)
 * SPACE COMPLEXITY: O(1)
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int>& nums) {
    if (nums.empty()) return 0;

    int max_sum = INT_MIN;
    for (int i = 0; i < (int)nums.size(); i++) {
        int current_sum = 0;
        for (int j = i; j < (int)nums.size(); j++) {
            current_sum += nums[j];
            max_sum = max(max_sum, current_sum);
        }
    }
    return max_sum;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    cout << solve(nums) << endl;
    return 0;
}
