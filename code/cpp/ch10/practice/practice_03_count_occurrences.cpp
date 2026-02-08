/*
 * Practice 3: Count Occurrences
 * ===============================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM:
 *   Given an array of integers and a target value, recursively count
 *   how many times target appears in the array.
 *
 * EXAMPLES:
 *   solve({1,2,3,2,4,2}, 2) -> 3
 *   solve({1,2,3}, 4)       -> 0
 *   solve({}, 1)             -> 0
 *
 * CONSTRAINTS:
 *   0 <= arr.size() <= 10^5
 *   -10^6 <= arr[i], target <= 10^6
 *
 * INSTRUCTIONS:
 *   Replace the body with your recursive solution.
 *   Hint: Use a helper function with an index parameter.
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
