/*
 * Challenge 3: Median of Two Sorted Arrays
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Find median of two sorted arrays in O(log(min(m,n))).
 */

#include <climits>
#include <iostream>
#include <vector>
using namespace std;

double solve(vector<int> nums1, vector<int> nums2) {
    // TODO: Replace this with your solution
    return 0.0;
}

int main() {
    int m, n;
    cin >> m;
    vector<int> nums1(m);
    for (int i = 0; i < m; i++) cin >> nums1[i];
    cin >> n;
    vector<int> nums2(n);
    for (int i = 0; i < n; i++) cin >> nums2[i];
    cout << solve(nums1, nums2) << endl;
    return 0;
}
