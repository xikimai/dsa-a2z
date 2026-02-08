/*
 * Practice 5: Generate All Subsets
 * ==================================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM:
 *   Given an array of distinct integers, return all possible subsets
 *   (the power set). The result should be sorted: each subset sorted
 *   internally, and subsets sorted lexicographically.
 *
 * EXAMPLES:
 *   solve({})      -> {{}}
 *   solve({1})     -> {{}, {1}}
 *   solve({1,2,3}) -> {{}, {1}, {1,2}, {1,2,3}, {1,3}, {2}, {2,3}, {3}}
 *
 * CONSTRAINTS:
 *   0 <= nums.size() <= 10
 *   All elements are distinct.
 *
 * INSTRUCTIONS:
 *   Replace the body with your recursive/backtracking solution.
 */

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> solve(vector<int> nums) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    vector<vector<int>> result = solve(nums);
    cout << "[";
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << ", ";
        cout << "[";
        for (int j = 0; j < (int)result[i].size(); j++) {
            if (j > 0) cout << ", ";
            cout << result[i][j];
        }
        cout << "]";
    }
    cout << "]" << endl;
    return 0;
}
