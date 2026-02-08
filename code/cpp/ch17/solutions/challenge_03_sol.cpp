/*
 * Solution for Challenge 3: Sliding Window Maximum
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Monotone decreasing deque of indices. For each element:
 *           1. Remove elements from back that are smaller.
 *           2. Add current index.
 *           3. Remove front if outside window.
 *           4. Front is always the max for current window.
 * TIME:  O(n) — each element enters/leaves the deque once
 * SPACE: O(k) for the deque
 */

#include <deque>
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> nums, int k) {
    deque<int> dq;  // Stores indices, monotone decreasing by value
    vector<int> result;

    for (int i = 0; i < (int)nums.size(); i++) {
        // Remove elements smaller than current from the back
        while (!dq.empty() && nums[dq.back()] <= nums[i]) {
            dq.pop_back();
        }
        dq.push_back(i);

        // Remove front if outside window
        if (dq.front() <= i - k) {
            dq.pop_front();
        }

        // Window is fully formed when i >= k - 1
        if (i >= k - 1) {
            result.push_back(nums[dq.front()]);
        }
    }
    return result;
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
