/*
 * Practice 2: Upper Bound
 * =========================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * PROBLEM:
 *   Given a SORTED array and a target, find the index of the first
 *   element that is STRICTLY GREATER than target. If no such element
 *   exists, return arr.size() (one past the end).
 *
 * EXAMPLES:
 *   solve({1,3,5,7,9}, 5) -> 3   (first element > 5 is 7 at index 3)
 *   solve({1,3,5,7,9}, 4) -> 2   (first element > 4 is 5 at index 2)
 *   solve({1,3,5,7,9}, 0) -> 0
 *   solve({1,3,5,7,9}, 9) -> 5   (no element > 9)
 *   solve({2,2,2,2}, 2)   -> 4
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
    return 0;
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
