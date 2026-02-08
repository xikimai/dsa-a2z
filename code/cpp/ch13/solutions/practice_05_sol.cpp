/*
 * Solution for Practice 5: Combination Sum
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * APPROACH: Sort, backtrack from index; allow reuse (i not i+1).
 * TIME:  O(n^(t/m))
 * SPACE: O(t/m)
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> solve(vector<int> candidates, int target) {
    sort(candidates.begin(), candidates.end());
    vector<vector<int>> result;
    vector<int> current;

    function<void(int, int)> backtrack = [&](int start, int remaining) {
        if (remaining == 0) {
            result.push_back(current);
            return;
        }
        for (int i = start; i < (int)candidates.size(); i++) {
            if (candidates[i] > remaining) break;  // Pruning
            current.push_back(candidates[i]);
            backtrack(i, remaining - candidates[i]);  // i, not i+1
            current.pop_back();
        }
    };

    backtrack(0, target);
    return result;
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
