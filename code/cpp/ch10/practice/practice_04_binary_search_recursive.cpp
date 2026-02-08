/*
 * Practice 4: Recursive Binary Search
 * ======================================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM:
 *   Given a sorted array and a target, return the index of target
 *   using recursive binary search. Return -1 if not found.
 *
 * EXAMPLES:
 *   solve({1,3,5,7,9}, 5) -> 2
 *   solve({1,3,5,7,9}, 4) -> -1
 *   solve({}, 1)           -> -1
 *
 * CONSTRAINTS:
 *   0 <= arr.size() <= 10^5
 *   Array is sorted in ascending order.
 *   -10^6 <= arr[i], target <= 10^6
 *
 * INSTRUCTIONS:
 *   Replace the body with your recursive solution.
 *   Hint: Use a helper function with lo and hi parameters.
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
