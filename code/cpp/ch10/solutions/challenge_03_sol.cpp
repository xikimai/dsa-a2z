/*
 * Solution -- Challenge 3: Combination Sum
 * ===========================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Sort candidates. Backtracking: at each step, try adding
 *           each candidate (reuse allowed). Use start index to avoid
 *           duplicate combinations. Prune when remaining < 0.
 * TIME:  O(n^(t/m)) where t=target, m=min candidate
 * SPACE: O(t/m) for recursion depth
 */

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void backtrack(const vector<int>& candidates, int target, int start,
               vector<int>& current, vector<vector<int>>& result) {
    if (target == 0) {
        result.push_back(current);
        return;
    }
    for (int i = start; i < (int)candidates.size(); i++) {
        if (candidates[i] > target) break;  // pruning (sorted)
        current.push_back(candidates[i]);
        backtrack(candidates, target - candidates[i], i, current, result);
        current.pop_back();
    }
}

vector<vector<int>> solve(vector<int> candidates, int target) {
    sort(candidates.begin(), candidates.end());
    vector<vector<int>> result;
    vector<int> current;
    backtrack(candidates, target, 0, current, result);
    sort(result.begin(), result.end());
    return result;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> candidates(n);
    for (int i = 0; i < n; i++) cin >> candidates[i];
    int target;
    cin >> target;
    vector<vector<int>> result = solve(candidates, target);
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
