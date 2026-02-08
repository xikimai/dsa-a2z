/*
 * Solution -- Challenge 2: Generate All Permutations
 * =====================================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Sort input first. Use backtracking with swap approach.
 *           Sort result to guarantee lexicographic order.
 * TIME:  O(n! * n)
 * SPACE: O(n! * n) for storing all permutations
 */

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void backtrack(vector<int>& nums, int start, vector<vector<int>>& result) {
    if (start == (int)nums.size()) {
        result.push_back(nums);
        return;
    }
    for (int i = start; i < (int)nums.size(); i++) {
        swap(nums[start], nums[i]);
        backtrack(nums, start + 1, result);
        swap(nums[start], nums[i]);
    }
}

vector<vector<int>> solve(vector<int> nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    backtrack(nums, 0, result);
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
