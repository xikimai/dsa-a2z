/*
 * Solution -- Practice 5: Generate All Subsets
 * ===============================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Sort input. Backtracking: at each index, include or exclude
 *           the current element. Sort result lexicographically.
 * TIME:  O(n * 2^n)
 * SPACE: O(n * 2^n) for storing all subsets
 */

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void backtrack(const vector<int>& nums, int idx, vector<int>& current,
               vector<vector<int>>& result) {
    if (idx == (int)nums.size()) {
        result.push_back(current);
        return;
    }
    // Include nums[idx]
    current.push_back(nums[idx]);
    backtrack(nums, idx + 1, current, result);
    current.pop_back();
    // Exclude nums[idx]
    backtrack(nums, idx + 1, current, result);
}

vector<vector<int>> solve(vector<int> nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    vector<int> current;
    backtrack(nums, 0, current, result);
    sort(result.begin(), result.end());
    return result;
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
