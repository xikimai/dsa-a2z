/*
 * Challenge 2: Single Element in Sorted Array
 * ==============================================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * PROBLEM:
 *   Given a sorted array where every element appears exactly twice
 *   except for one element that appears once, find that single element.
 *   Must run in O(log n) time.
 *
 * EXAMPLES:
 *   solve({1,1,2,3,3,4,4,8,8}) -> 2
 *   solve({3,3,7,7,10,11,11})  -> 10
 *   solve({1})                 -> 1
 *   solve({1,1,2})             -> 2
 *   solve({1,2,2})             -> 1
 *
 * CONSTRAINTS:
 *   1 <= arr.size() <= 10^5
 *   arr.size() is always odd
 *   Array is sorted in non-decreasing order
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
