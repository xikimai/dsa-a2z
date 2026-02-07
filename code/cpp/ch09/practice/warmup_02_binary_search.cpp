/*
 * Warmup 2: Binary Search
 * =========================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * PROBLEM:
 *   Given a SORTED array and a target value, return the index of
 *   the target using binary search. If not found, return -1.
 *
 * EXAMPLES:
 *   solve({1,3,5,7,9,11}, 7)  -> 3
 *   solve({1,3,5,7,9,11}, 4)  -> -1
 *   solve({2,4,6,8,10}, 2)    -> 0
 *   solve({2,4,6,8,10}, 10)   -> 4
 *
 * CONSTRAINTS:
 *   0 <= arr.size() <= 10^5
 *   Array is sorted in non-decreasing order
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution.
 *   Do NOT use std::binary_search or std::lower_bound.
 */

#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> arr, int target) {
    // TODO: Replace this with your solution
    return -1;
}

// -- Do not change anything below this line --------------------------
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
