/*
 * Challenge 2: Generate All Permutations
 * =========================================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM:
 *   Given an array of distinct integers, return all possible permutations.
 *   The result should be sorted lexicographically.
 *
 * EXAMPLES:
 *   solve({1,2,3}) -> {{1,2,3}, {1,3,2}, {2,1,3}, {2,3,1}, {3,1,2}, {3,2,1}}
 *   solve({1})     -> {{1}}
 *   solve({0,1})   -> {{0,1}, {1,0}}
 *
 * CONSTRAINTS:
 *   1 <= nums.size() <= 8
 *   All elements are distinct.
 *
 * INSTRUCTIONS:
 *   Replace the body with your backtracking solution.
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
