/*
 * Practice 3: Floor and Ceil
 * ============================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * PROBLEM:
 *   Given a SORTED array and a target, find the floor and ceil.
 *   - Floor: the largest element <= target (or -1 if none)
 *   - Ceil:  the smallest element >= target (or -1 if none)
 *   Return them as a vector {floor, ceil}.
 *
 * EXAMPLES:
 *   solve({1,3,5,7,9}, 5)  -> {5, 5}
 *   solve({1,3,5,7,9}, 4)  -> {3, 5}
 *   solve({1,3,5,7,9}, 0)  -> {-1, 1}
 *   solve({1,3,5,7,9}, 10) -> {9, -1}
 *   solve({1}, 1)           -> {1, 1}
 *
 * CONSTRAINTS:
 *   0 <= arr.size() <= 10^5
 *   Array is sorted in non-decreasing order
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution.
 */

#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr, int target) {
    // TODO: Replace this with your solution
    return {-1, -1};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    int target;
    cin >> target;
    vector<int> result = solve(arr, target);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}
