/*
 * Warmup 4: Last Occurrence
 * ===========================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * PROBLEM:
 *   Given a SORTED array and a target, find the index of the LAST
 *   (rightmost) occurrence of target. Return -1 if not found.
 *
 * EXAMPLES:
 *   solve({1,2,2,2,3,4}, 2) -> 3
 *   solve({1,1,1,1,1}, 1)   -> 4
 *   solve({1,3,5,7}, 5)     -> 2
 *   solve({1,3,5,7}, 4)     -> -1
 *
 * CONSTRAINTS:
 *   0 <= arr.size() <= 10^5
 *   Array is sorted in non-decreasing order
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution.
 *   Do NOT use std::upper_bound.
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
