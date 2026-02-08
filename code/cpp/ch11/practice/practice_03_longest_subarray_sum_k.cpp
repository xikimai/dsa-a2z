/*
 * Practice 3: Longest Subarray with Sum K
 * =========================================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM:
 *   Given an array of integers and a target sum k, find the length of
 *   the longest contiguous subarray whose elements sum to k.
 *   Use prefix sum + hash map approach.
 *
 * EXAMPLES:
 *   solve({1,2,3,1,1,1,1}, 3)  -> 3
 *   solve({-1,1,1}, 1)         -> 3
 *   solve({1,2,3}, 10)         -> 0
 *   solve({1,-1,1,-1,1}, 0)    -> 4
 *
 * CONSTRAINTS:
 *   - 1 <= arr.size() <= 10^5
 *   - -10^5 <= arr[i] <= 10^5
 *   - -10^9 <= k <= 10^9
 *
 * INSTRUCTIONS:
 *   Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

int solve(vector<int> arr, int k) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n, k;
    cin >> n >> k;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << solve(arr, k) << endl;
    return 0;
}
