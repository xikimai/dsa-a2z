/*
 * Challenge 4: Kth Element of Two Sorted Arrays
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Find the kth smallest element (1-indexed) from two sorted arrays.
 */

#include <climits>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> nums1, vector<int> nums2, int k) {
    // TODO: Replace this with your solution
    return 0;
}

int main() {
    int m, n, k;
    cin >> m;
    vector<int> nums1(m);
    for (int i = 0; i < m; i++) cin >> nums1[i];
    cin >> n;
    vector<int> nums2(n);
    for (int i = 0; i < n; i++) cin >> nums2[i];
    cin >> k;
    cout << solve(nums1, nums2, k) << endl;
    return 0;
}
