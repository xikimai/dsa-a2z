/*
 * Warmup 1: Linear Search
 * =========================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * PROBLEM:
 *   Given an array and a target value, return the index of the first
 *   occurrence of target. If target is not found, return -1.
 *
 * EXAMPLES:
 *   solve({1,3,5,7,9}, 5) -> 2
 *   solve({1,3,5,7,9}, 4) -> -1
 *   solve({2,2,2,2}, 2)   -> 0
 *
 * CONSTRAINTS:
 *   0 <= arr.size() <= 10^5
 *   -10^6 <= arr[i] <= 10^6
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution.
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
