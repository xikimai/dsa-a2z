/*
 * Challenge 3: Search in Rotated Sorted Array II (with duplicates)
 * ==================================================================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * PROBLEM:
 *   Given a rotated sorted array that MAY CONTAIN DUPLICATES and a
 *   target, return true if target exists in the array, false otherwise.
 *
 * EXAMPLES:
 *   solve({2,5,6,0,0,1,2}, 0) -> true
 *   solve({2,5,6,0,0,1,2}, 3) -> false
 *   solve({1,0,1,1,1}, 0)     -> true
 *   solve({1,1,1,1,1}, 2)     -> false
 *   solve({1}, 1)             -> true
 *
 * CONSTRAINTS:
 *   1 <= arr.size() <= 10^5
 *   Array may contain duplicates
 *
 * NOTE:
 *   Worst case is O(n) due to duplicates, but average is O(log n).
 *   When arr[lo] == arr[mid] == arr[hi], we can't determine which
 *   half is sorted, so we shrink both ends.
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution.
 */

#include <iostream>
#include <vector>
using namespace std;

bool solve(vector<int> arr, int target) {
    // TODO: Replace this with your solution
    return false;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    int target;
    cin >> target;
    cout << (solve(arr, target) ? "true" : "false") << endl;
    return 0;
}
