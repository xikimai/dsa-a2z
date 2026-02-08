/*
 * Example 02: Monotonic Stack — Next Greater Element & Histogram
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * Demonstrates:
 *   - Next Greater Element with monotonic stack
 *   - Largest Rectangle in Histogram
 *   - Sliding Window Maximum with deque
 *
 * Build: g++ -std=c++17 -o /tmp/ex02_ch22 code/cpp/ch22/learn/example_02_monotonic_stack.cpp && /tmp/ex02_ch22
 */

#include <algorithm>
#include <deque>
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

void nextGreaterDemo() {
    cout << "=== Next Greater Element ===" << endl;
    vector<int> arr = {4, 5, 2, 10, 8};
    int n = arr.size();
    vector<int> result(n, -1);
    stack<int> stk;

    for (int i = n - 1; i >= 0; i--) {
        while (!stk.empty() && arr[stk.top()] <= arr[i]) stk.pop();
        if (!stk.empty()) result[i] = arr[stk.top()];
        stk.push(i);
    }

    cout << "  Input:  ";
    for (int x : arr) cout << x << " ";
    cout << endl << "  Result: ";
    for (int x : result) cout << x << " ";
    cout << endl << endl;
}

void histogramDemo() {
    cout << "=== Largest Rectangle in Histogram ===" << endl;
    vector<int> heights = {2, 1, 5, 6, 2, 3};
    stack<int> stk;
    int maxArea = 0;
    int n = heights.size();

    for (int i = 0; i <= n; i++) {
        int curr = (i == n) ? 0 : heights[i];
        while (!stk.empty() && heights[stk.top()] > curr) {
            int h = heights[stk.top()]; stk.pop();
            int w = stk.empty() ? i : i - stk.top() - 1;
            maxArea = max(maxArea, h * w);
        }
        stk.push(i);
    }

    cout << "  Heights: ";
    for (int x : heights) cout << x << " ";
    cout << endl << "  Max area: " << maxArea << endl << endl;
}

void slidingWindowDemo() {
    cout << "=== Sliding Window Maximum ===" << endl;
    vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    deque<int> dq;
    vector<int> result;

    for (int i = 0; i < (int)nums.size(); i++) {
        while (!dq.empty() && dq.front() < i - k + 1) dq.pop_front();
        while (!dq.empty() && nums[dq.back()] <= nums[i]) dq.pop_back();
        dq.push_back(i);
        if (i >= k - 1) result.push_back(nums[dq.front()]);
    }

    cout << "  Input: ";
    for (int x : nums) cout << x << " ";
    cout << ", k=" << k << endl << "  Result: ";
    for (int x : result) cout << x << " ";
    cout << endl;
}

int main() {
    nextGreaterDemo();
    histogramDemo();
    slidingWindowDemo();
    return 0;
}
