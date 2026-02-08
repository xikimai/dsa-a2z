/*
 * Practice 2: Subarray Sum Equals K (Count)
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Count subarrays with sum equal to k.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int solve(vector<int> arr, int k) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n, k;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    cin >> k;
    cout << solve(arr, k) << endl;
    return 0;
}
