/* Solution: Challenge 2 — Trapping Rain Water (Ch 15) */
#include <algorithm>
#include <vector>
using namespace std;
int solve(vector<int> heights) {
    if ((int)heights.size() < 3) return 0;
    int left = 0, right = (int)heights.size() - 1;
    int leftMax = heights[left], rightMax = heights[right];
    int water = 0;
    while (left < right) {
        if (leftMax <= rightMax) {
            left++;
            leftMax = max(leftMax, heights[left]);
            water += leftMax - heights[left];
        } else {
            right--;
            rightMax = max(rightMax, heights[right]);
            water += rightMax - heights[right];
        }
    }
    return water;
}
