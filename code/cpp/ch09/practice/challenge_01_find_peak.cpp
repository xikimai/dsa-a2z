/*
 * Challenge 1: Find Peak Element
 * =================================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * PROBLEM:
 *   A peak element is strictly greater than its neighbors.
 *   arr[-1] = arr[n] = -infinity (boundaries are treated as -inf).
 *   Find ANY peak element's index.
 *
 *   Implement THREE approaches:
 *     solve_linear(arr) -- O(n) linear scan
 *     solve_binary(arr) -- O(log n) binary search
 *     solve(arr)        -- calls solve_binary
 *
 * EXAMPLES:
 *   solve({1,2,3,1})       -> 2  (arr[2]=3 is a peak)
 *   solve({1,2,1,3,5,6,4}) -> 1 or 5  (multiple valid answers)
 *   solve({1})             -> 0
 *   solve({3,2,1})         -> 0
 *   solve({1,2,3})         -> 2
 *
 * CONSTRAINTS:
 *   1 <= arr.size() <= 10^5
 *   arr[i] != arr[i+1] for all valid i (no adjacent equal elements)
 *
 * INSTRUCTIONS:
 *   Replace all three function bodies with your solutions.
 */

#include <iostream>
#include <vector>
using namespace std;

int solve_linear(vector<int> arr) {
    // TODO: Replace this with your O(n) solution
    return 0;
}

int solve_binary(vector<int> arr) {
    // TODO: Replace this with your O(log n) solution
    return 0;
}

int solve(vector<int> arr) {
    // TODO: Call solve_binary
    return solve_binary(arr);
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
