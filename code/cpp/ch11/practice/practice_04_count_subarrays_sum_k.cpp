/*
 * Practice 4: Count Subarrays with Sum K
 * ========================================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM:
 *   Given an array of integers and a target sum k, count the total
 *   number of contiguous subarrays whose sum equals k.
 *   Use prefix sum + frequency map. Initialise with {0: 1}.
 *
 * EXAMPLES:
 *   solve({1,1,1}, 2)     -> 2
 *   solve({1,2,3}, 3)     -> 2
 *   solve({1}, 0)          -> 0
 *   solve({1,-1,0}, 0)     -> 3
 *   solve({0,0,0}, 0)      -> 6
 *
 * CONSTRAINTS:
 *   - 1 <= arr.size() <= 10^5
 *   - -10^5 <= arr[i] <= 10^5
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
