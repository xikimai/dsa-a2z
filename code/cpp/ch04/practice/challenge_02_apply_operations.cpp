/*
 * Challenge 2: Apply Operations
 * =============================
 * Chapter 4: Functions
 *
 * PROBLEM:
 *   Given a vector of integers and a vector of operation names,
 *   apply each operation to the vector in order and return the result.
 *
 *   Supported operations:
 *     "double"  — multiply every element by 2
 *     "negate"  — multiply every element by -1
 *     "sort"    — sort in ascending order
 *     "reverse" — reverse the order
 *     "square"  — replace each element with its square
 *
 *   Ignore any unrecognized operations.
 *
 * EXAMPLES:
 *   solve({1,2,3}, {"double"})             -> {2, 4, 6}
 *   solve({3,1,2}, {"sort"})               -> {1, 2, 3}
 *   solve({1,2,3}, {"double", "reverse"})  -> {6, 4, 2}
 *   solve({3,1,2}, {"sort", "negate"})     -> {-1, -2, -3}
 *   solve({1,2,3}, {"square", "sort"})     -> {1, 4, 9}
 *   solve({1,2,3}, {"unknown"})            -> {1, 2, 3}
 *   solve({}, {"double"})                  -> {}
 *
 * CONSTRAINTS:
 *   - Operations are applied left to right
 *   - Unknown operations are silently ignored
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// TODO: Write helper functions for each operation

/**
 * Applies the operations to nums in order and returns the result.
 */
vector<int> solve(vector<int> nums, vector<string> operations) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    int m;
    cin >> m;
    vector<string> operations(m);
    for (int i = 0; i < m; i++) {
        cin >> operations[i];
    }
    vector<int> result = solve(nums, operations);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
