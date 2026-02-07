/*
 * Warmup 5: Count Occurrences
 * ==============================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * PROBLEM:
 *   Given a SORTED array and a target, count how many times target
 *   appears in the array.
 *
 * EXAMPLES:
 *   solve({1,2,2,2,3,4}, 2) -> 3
 *   solve({1,1,1,1,1}, 1)   -> 5
 *   solve({1,3,5,7}, 5)     -> 1
 *   solve({1,3,5,7}, 4)     -> 0
 *
 * CONSTRAINTS:
 *   0 <= arr.size() <= 10^5
 *   Array is sorted in non-decreasing order
 *
 * HINT:
 *   Use first occurrence and last occurrence to get O(log n).
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution.
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
