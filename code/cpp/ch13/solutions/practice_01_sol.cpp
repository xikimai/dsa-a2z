/*
 * Solution for Practice 1: Subsets Using Bitmasks
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * APPROACH: Iterate masks 0..2^n-1, check bits.
 * TIME:  O(2^n * n)
 * SPACE: O(2^n * n)
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> solve(vector<int> nums) {
    sort(nums.begin(), nums.end());
    int n = nums.size();
    vector<vector<int>> result;
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<int> subset;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                subset.push_back(nums[i]);
            }
        }
        result.push_back(subset);
    }
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
