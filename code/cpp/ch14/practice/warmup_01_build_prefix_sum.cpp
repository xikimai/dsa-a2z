/*
 * Warmup 1: Build Prefix Sum Array
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Given an integer array, build the prefix sum array.
 *          prefix[0] = 0, prefix[i] = arr[0] + ... + arr[i-1].
 *
 * EXAMPLES:
 *   solve({3,1,4,1,5}) -> {0, 3, 4, 8, 9, 14}
 *   solve({5})          -> {0, 5}
 *   solve({})           -> {0}
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

vector<long long> solve(vector<int> arr) {
    // TODO: Replace this with your solution
    return {0};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    auto result = solve(arr);
    for (int i = 0; i < (int)result.size(); i++)
        cout << result[i] << (i < (int)result.size()-1 ? " " : "\n");
    return 0;
}
