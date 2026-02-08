/*
 * Practice 5: Combination Sum
 * ====================================
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * PROBLEM:
 *   Find all unique combinations of candidates that sum to target.
 *   Each number may be reused unlimited times.
 *
 * EXAMPLES:
 *   solve({2,3,6,7}, 7) -> {{2,2,3},{7}}
 *
 * CONSTRAINTS:
 *   - 1 <= candidates.size() <= 10
 *   - 1 <= candidates[i] <= 30
 *   - 1 <= target <= 30
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> solve(vector<int> candidates, int target) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n, target;
    cin >> n;
    vector<int> candidates(n);
    for (int i = 0; i < n; i++) cin >> candidates[i];
    cin >> target;
    vector<vector<int>> result = solve(candidates, target);
    for (auto& combo : result) {
        for (int i = 0; i < (int)combo.size(); i++) {
            if (i > 0) cout << " ";
            cout << combo[i];
        }
        cout << endl;
    }
    return 0;
}
