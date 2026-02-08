/*
 * Solution for Challenge 2: Trapping Rain Water
 * Chapter 22: Stacks & Queues — Order Matters
 * APPROACH: Two-pointer with left_max and right_max.
 * TIME: O(n), SPACE: O(1)
 */
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> height) {
    int n = height.size();
    if (n < 3) return 0;
    int left = 0, right = n - 1;
    int leftMax = height[left], rightMax = height[right];
    int water = 0;
    while (left < right) {
        if (leftMax <= rightMax) {
            left++;
            leftMax = max(leftMax, height[left]);
            water += leftMax - height[left];
        } else {
            right--;
            rightMax = max(rightMax, height[right]);
            water += rightMax - height[right];
        }
    }
    return water;
}

int main() {
    int n;
    cin >> n;
    vector<int> height(n);
    for (int i = 0; i < n; i++) cin >> height[i];
    cout << solve(height) << endl;
    return 0;
}
