/*
 * Practice 1: Top K Frequent Elements
 * =====================================
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM:
 *   Given an integer array nums and an integer k, return the k most
 *   frequent elements. Return them sorted in ascending order.
 *
 * EXAMPLES:
 *   solve({1,1,1,2,2,3}, 2)  -> {1,2}
 *   solve({1}, 1)             -> {1}
 *
 * CONSTRAINTS:
 *   - 1 <= nums.size() <= 10^5
 *   - 1 <= k <= number of unique elements
 *
 * INSTRUCTIONS:
 *   Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <iostream>
#include <queue>
#include <unordered_map>
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
