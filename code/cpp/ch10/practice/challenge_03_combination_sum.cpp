/*
 * Challenge 3: Combination Sum
 * ==============================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM:
 *   Given an array of distinct positive integers (candidates) and a target,
 *   find all unique combinations where the candidates sum to target.
 *   The same number may be used UNLIMITED times.
 *   Return combinations sorted: each combination sorted internally,
 *   and the list of combinations sorted lexicographically.
 *
 * EXAMPLES:
 *   solve({2,3,6,7}, 7)  -> {{2,2,3}, {7}}
 *   solve({2,3,5}, 8)    -> {{2,2,2,2}, {2,3,3}, {3,5}}
 *   solve({2}, 1)         -> {}
 *
 * CONSTRAINTS:
 *   1 <= candidates.size() <= 30
 *   2 <= candidates[i] <= 40
 *   1 <= target <= 40
 *   All candidates are distinct.
 *
 * INSTRUCTIONS:
 *   Replace the body with your backtracking solution.
 */

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> solve(vector<int> candidates, int target) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> candidates(n);
    for (int i = 0; i < n; i++) cin >> candidates[i];
    int target;
    cin >> target;
    vector<vector<int>> result = solve(candidates, target);
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
