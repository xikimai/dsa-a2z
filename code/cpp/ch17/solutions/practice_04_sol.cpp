/*
 * Solution for Practice 4: Find Median from Data Stream
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Two heaps: max-heap for lower half, min-heap for upper half.
 *           Max-heap can have at most 1 more element than min-heap.
 *           Median is either top of max-heap (odd) or average of both tops (even).
 * TIME:  O(n log n) total — O(log n) per add
 * SPACE: O(n)
 */

#include <functional>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<double> solve(vector<int> nums) {
    priority_queue<int> maxHeap;                                    // Lower half
    priority_queue<int, vector<int>, greater<int>> minHeap;         // Upper half
    vector<double> medians;

    for (int num : nums) {
        // Add to max-heap (lower half)
        maxHeap.push(num);

        // Ensure max of lower half <= min of upper half
        if (!minHeap.empty() && maxHeap.top() > minHeap.top()) {
            int val = maxHeap.top(); maxHeap.pop();
            minHeap.push(val);
        }

        // Balance sizes
        if ((int)maxHeap.size() > (int)minHeap.size() + 1) {
            int val = maxHeap.top(); maxHeap.pop();
            minHeap.push(val);
        } else if ((int)minHeap.size() > (int)maxHeap.size()) {
            int val = minHeap.top(); minHeap.pop();
            maxHeap.push(val);
        }

        // Calculate median
        if (maxHeap.size() > minHeap.size()) {
            medians.push_back((double)maxHeap.top());
        } else {
            medians.push_back((maxHeap.top() + minHeap.top()) / 2.0);
        }
    }
    return medians;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    vector<double> result = solve(nums);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
