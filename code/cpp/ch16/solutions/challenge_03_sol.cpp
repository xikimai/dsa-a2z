/* Solution: Challenge 3 — Median of Two Sorted Arrays (Ch 16) */
#include <algorithm>
#include <climits>
#include <vector>
using namespace std;
double solve(vector<int> nums1, vector<int> nums2) {
    if (nums1.size() > nums2.size()) swap(nums1, nums2);
    int m = nums1.size(), n = nums2.size();
    int half = (m + n + 1) / 2;
    int lo = 0, hi = m;
    while (lo <= hi) {
        int i = lo + (hi - lo) / 2;
        int j = half - i;
        int left1 = (i > 0) ? nums1[i - 1] : INT_MIN;
        int left2 = (j > 0) ? nums2[j - 1] : INT_MIN;
        int right1 = (i < m) ? nums1[i] : INT_MAX;
        int right2 = (j < n) ? nums2[j] : INT_MAX;
        if (left1 <= right2 && left2 <= right1) {
            if ((m + n) % 2 == 1) return max(left1, left2);
            else return (max(left1, left2) + min(right1, right2)) / 2.0;
        } else if (left1 > right2) {
            hi = i - 1;
        } else {
            lo = i + 1;
        }
    }
    return 0.0;
}
