/*
 * Warmup 1: Kth Largest Element
 * ==============================
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM:
 *   Given an integer array nums and an integer k, return the kth largest
 *   element in the array.
 *
 * EXAMPLES:
 *   solve({3,2,1,5,6,4}, 2)             -> 5
 *   solve({3,2,3,1,2,4,5,5,6}, 4)       -> 4
 *
 * CONSTRAINTS:
 *   - 1 <= k <= nums.size() <= 10^4
 *   - -10^4 <= nums[i] <= 10^4
 *
 * INSTRUCTIONS:
 *   Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int solve(vector<int> nums, int k) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n, k;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    cin >> k;
    cout << solve(nums, k) << endl;
    return 0;
}
