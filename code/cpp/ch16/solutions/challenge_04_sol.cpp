/* Solution: Challenge 4 — Kth Element of Two Sorted Arrays (Ch 16) */
#include <algorithm>
#include <climits>
#include <vector>
using namespace std;
int solve(vector<int> nums1, vector<int> nums2, int k) {
    if (nums1.size() > nums2.size()) return solve(nums2, nums1, k);
    int m = nums1.size(), n = nums2.size();
    int lo = max(0, k - n);
    int hi = min(k, m);
    while (lo <= hi) {
        int i = lo + (hi - lo) / 2;
        int j = k - i;
        int left1 = (i > 0) ? nums1[i - 1] : INT_MIN;
        int left2 = (j > 0) ? nums2[j - 1] : INT_MIN;
        int right1 = (i < m) ? nums1[i] : INT_MAX;
        int right2 = (j < n) ? nums2[j] : INT_MAX;
        if (left1 <= right2 && left2 <= right1) {
            return max(left1, left2);
        } else if (left1 > right2) {
            hi = i - 1;
        } else {
            lo = i + 1;
        }
    }
    return -1;
}
