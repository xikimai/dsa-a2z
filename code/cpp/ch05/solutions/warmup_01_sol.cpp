/*
 * Solution -- Warmup 1: Second Largest
 * =====================================
 * Chapter 5: Collections
 *
 * APPROACH:
 *   Single pass tracking the largest and second largest values.
 *   Initialize both to INT_MIN (or use a flag). As we scan, if we find
 *   something bigger than first, shift first -> second, update first.
 *   If it's between first and second (and != first), update second.
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(1)
 */

#include <climits>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int>& nums) {
    if (nums.size() < 2) return -1;

    int first = INT_MIN;
    int second = INT_MIN;

    for (int x : nums) {
        if (x > first) {
            second = first;
            first = x;
        } else if (x > second && x != first) {
            second = x;
        }
    }

    return (second == INT_MIN) ? -1 : second;
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
