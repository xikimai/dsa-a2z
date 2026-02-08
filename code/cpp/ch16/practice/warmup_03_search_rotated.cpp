/*
 * Warmup 3: Search in Rotated Sorted Array
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Given rotated sorted array (no duplicates) and target,
 *          return index of target or -1.
 */

#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> arr, int target) {
    // TODO: Replace this with your solution
    return -1;
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    int target;
    cin >> target;
    cout << solve(arr, target) << endl;
    return 0;
}
