/*
 * Solution for Challenge 3: N-Queens All Solutions
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * APPROACH: Backtrack row-by-row, build board strings for each solution.
 * TIME:  O(n!)
 * SPACE: O(n^2)
 */

#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

vector<vector<string>> solve(int n) {
    vector<vector<string>> result;
    vector<int> queens;
    set<int> cols, d1, d2;

    function<void(int)> backtrack = [&](int row) {
        if (row == n) {
            vector<string> board;
            for (int r = 0; r < n; r++) {
                string row_str(n, '.');
                row_str[queens[r]] = 'Q';
                board.push_back(row_str);
            }
            result.push_back(board);
            return;
        }
        for (int col = 0; col < n; col++) {
            if (cols.count(col) || d1.count(row - col) || d2.count(row + col))
                continue;
            cols.insert(col);
            d1.insert(row - col);
            d2.insert(row + col);
            queens.push_back(col);
            backtrack(row + 1);
            queens.pop_back();
            cols.erase(col);
            d1.erase(row - col);
            d2.erase(row + col);
        }
    };

    backtrack(0);
    sort(result.begin(), result.end());
    return result;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<vector<string>> result = solve(n);
    for (auto& sol : result) {
        for (auto& row : sol) cout << row << endl;
        cout << endl;
    }
    return 0;
}
