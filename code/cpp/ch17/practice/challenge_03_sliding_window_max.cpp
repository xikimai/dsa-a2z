/*
 * Challenge 3: Sliding Window Maximum
 * ======================================
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM:
 *   Given an integer array nums and a window size k, return the maximum
 *   value in each sliding window of size k as it moves left to right.
 *
 * EXAMPLES:
 *   solve({1,3,-1,-3,5,3,6,7}, 3)  -> {3,3,5,5,6,7}
 *   solve({1}, 1)                   -> {1}
 *
 * CONSTRAINTS:
 *   - 1 <= nums.size() <= 10^5
 *   - 1 <= k <= nums.size()
 *   - -10^4 <= nums[i] <= 10^4
 *
 * INSTRUCTIONS:
 *   Replace the body of solve() with your solution.
 */

#include <deque>
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> nums, int k) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n, k;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    cin >> k;
    vector<int> result = solve(nums, k);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
