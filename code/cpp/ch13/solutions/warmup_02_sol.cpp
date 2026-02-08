/*
 * Solution for Warmup 2: Generate All Subsets
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * APPROACH: Recursion — include or exclude each element.
 * TIME:  O(2^n * n)
 * SPACE: O(n)
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> solve(vector<int> nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    vector<int> current;

    function<void(int)> backtrack = [&](int index) {
        if (index == (int)nums.size()) {
            result.push_back(current);
            return;
        }
        // Exclude
        backtrack(index + 1);
        // Include
        current.push_back(nums[index]);
        backtrack(index + 1);
        current.pop_back();
    };

    backtrack(0);
    sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b) {
        if (a.size() != b.size()) return a.size() < b.size();
        return a < b;
    });
    return result;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    vector<vector<int>> result = solve(nums);
    for (auto& s : result) {
        for (int i = 0; i < (int)s.size(); i++) {
            if (i > 0) cout << " ";
            cout << s[i];
        }
        cout << endl;
    }
    return 0;
}
