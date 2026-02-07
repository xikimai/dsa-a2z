/*
 * Practice 5: Find Minimum in Rotated Sorted Array
 * ===================================================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * PROBLEM:
 *   Given a rotated sorted array (no duplicates), find the minimum
 *   element. Return the VALUE (not the index).
 *
 * EXAMPLES:
 *   solve({3,4,5,1,2})       -> 1
 *   solve({4,5,6,7,0,1,2})   -> 0
 *   solve({1})               -> 1
 *   solve({2,1})             -> 1
 *   solve({1,2,3,4,5})       -> 1
 *
 * CONSTRAINTS:
 *   1 <= arr.size() <= 10^5
 *   All elements are unique
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution. Must be O(log n).
 */

#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> arr) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << solve(arr) << endl;
    return 0;
}
