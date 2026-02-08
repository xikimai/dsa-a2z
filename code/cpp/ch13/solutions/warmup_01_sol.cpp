/*
 * Solution for Warmup 1: Generate All Permutations
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * APPROACH: Sort, then backtrack with a 'used' array.
 * TIME:  O(n! * n)
 * SPACE: O(n)
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> solve(vector<int> nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    vector<bool> used(nums.size(), false);
    vector<int> current;

    function<void()> backtrack = [&]() {
        if ((int)current.size() == (int)nums.size()) {
            result.push_back(current);
            return;
        }
        for (int i = 0; i < (int)nums.size(); i++) {
            if (used[i]) continue;
            used[i] = true;
            current.push_back(nums[i]);
            backtrack();
            current.pop_back();
            used[i] = false;
        }
    };

    backtrack();
    return result;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    vector<vector<int>> result = solve(nums);
    for (auto& perm : result) {
        for (int i = 0; i < (int)perm.size(); i++) {
            if (i > 0) cout << " ";
            cout << perm[i];
        }
        cout << endl;
    }
    return 0;
}
