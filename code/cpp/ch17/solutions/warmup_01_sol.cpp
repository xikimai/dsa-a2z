/*
 * Solution for Warmup 1: Kth Largest Element
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Use a min-heap of size k. Push each element; if size exceeds k,
 *           pop the smallest. The root is the kth largest.
 * TIME:  O(n log k)
 * SPACE: O(k)
 */

#include <algorithm>
#include <functional>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int solve(vector<int> nums, int k) {
    // Min-heap: smallest element on top
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int x : nums) {
        pq.push(x);
        if ((int)pq.size() > k) pq.pop();
    }
    return pq.top();
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
