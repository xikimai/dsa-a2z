/*
 * Practice 4: Power Set Using Bitmasks
 * Chapter 12: Bit Manipulation — The Language of Computers
 *
 * PROBLEM: Return all subsets using bitmask iteration.
 * EXAMPLES: solve({1,2,3}) -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
 * CONSTRAINTS: 0 <= nums.size() <= 10
 */

#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> solve(vector<int> nums) {
    // TODO: Replace this with your solution
    return {};
}

int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    vector<vector<int>> result = solve(nums);
    for (auto& subset : result) {
        cout << "[";
        for (int j = 0; j < (int)subset.size(); j++) {
            if (j > 0) cout << ",";
            cout << subset[j];
        }
        cout << "]" << endl;
    }
    return 0;
}
