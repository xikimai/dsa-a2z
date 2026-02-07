/*
 * Practice 4: Search in Rotated Sorted Array
 * =============================================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * PROBLEM:
 *   Given a rotated sorted array (no duplicates) and a target,
 *   return the index of target. Return -1 if not found.
 *   A rotated sorted array is a sorted array that has been rotated
 *   at some pivot (e.g., {4,5,6,7,0,1,2} was {0,1,2,4,5,6,7}).
 *
 * EXAMPLES:
 *   solve({4,5,6,7,0,1,2}, 0) -> 4
 *   solve({4,5,6,7,0,1,2}, 3) -> -1
 *   solve({1}, 1)              -> 0
 *   solve({3,1,2}, 1)         -> 1
 *
 * CONSTRAINTS:
 *   1 <= arr.size() <= 10^5
 *   All elements are unique
 *   Array is a rotated sorted array
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution. Must be O(log n).
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
