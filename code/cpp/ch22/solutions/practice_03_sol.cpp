/*
 * Solution for Practice 3: Sliding Window Maximum
 * Chapter 22: Stacks & Queues — Order Matters
 * APPROACH: Deque maintaining decreasing order of values.
 * TIME: O(n), SPACE: O(k)
 */
#include <deque>
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> nums, int k) {
    deque<int> dq;
    vector<int> result;
    for (int i = 0; i < (int)nums.size(); i++) {
        while (!dq.empty() && dq.front() < i - k + 1) dq.pop_front();
        while (!dq.empty() && nums[dq.back()] <= nums[i]) dq.pop_back();
        dq.push_back(i);
        if (i >= k - 1) result.push_back(nums[dq.front()]);
    }
    return result;
}

int main() {
    int n, k;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    cin >> k;
    for (int x : solve(nums, k)) cout << x << " ";
    cout << endl;
    return 0;
}
