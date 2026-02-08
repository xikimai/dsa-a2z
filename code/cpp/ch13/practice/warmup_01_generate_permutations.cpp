/*
 * Warmup 1: Generate All Permutations
 * ====================================
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * PROBLEM:
 *   Given a vector of distinct integers, return all permutations
 *   sorted in lexicographic order.
 *
 * EXAMPLES:
 *   solve({1,2,3}) -> {{1,2,3},{1,3,2},{2,1,3},{2,3,1},{3,1,2},{3,2,1}}
 *   solve({0,1})   -> {{0,1},{1,0}}
 *
 * CONSTRAINTS:
 *   - 1 <= nums.size() <= 8
 *   - All elements are distinct
 *
 * INSTRUCTIONS:
 *   Replace the body of solve() with your solution.
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
    for (auto& perm : result) {
        for (int i = 0; i < (int)perm.size(); i++) {
            if (i > 0) cout << " ";
            cout << perm[i];
        }
        cout << endl;
    }
    return 0;
}
