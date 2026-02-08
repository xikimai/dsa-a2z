/*
 * Warmup 4: Peak Element in Array
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Find index of any peak element (greater than its neighbors).
 *          Treat out-of-bounds as negative infinity.
 */

#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> arr) {
    // TODO: Replace this with your solution
    return -1;
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << solve(arr) << endl;
    return 0;
}
