/*
 * Warmup 2: Generate All Subsets
 * ====================================
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * PROBLEM:
 *   Given a vector of distinct integers, return all subsets
 *   sorted by size then lexicographically.
 *
 * EXAMPLES:
 *   solve({1,2,3}) -> {{},{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}
 *   solve({0})     -> {{},{0}}
 *
 * CONSTRAINTS:
 *   - 0 <= nums.size() <= 10
 *   - All elements are distinct
 */

#include <algorithm>
#include <iostream>
#include <vector>
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
    for (auto& s : result) {
        for (int i = 0; i < (int)s.size(); i++) {
            if (i > 0) cout << " ";
            cout << s[i];
        }
        cout << endl;
    }
    return 0;
}
