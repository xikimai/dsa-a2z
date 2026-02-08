/*
 * Solution for Challenge 1: Largest Rectangle in Histogram
 * Chapter 22: Stacks & Queues — Order Matters
 * APPROACH: Monotonic stack (increasing). Sentinel flushes at end.
 * TIME: O(n), SPACE: O(n)
 */
#include <algorithm>
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int solve(vector<int> heights) {
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
    return maxArea;
}

int main() {
    int n;
    cin >> n;
    vector<int> heights(n);
    for (int i = 0; i < n; i++) cin >> heights[i];
    cout << solve(heights) << endl;
    return 0;
}
