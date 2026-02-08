/*
 * Solution for Practice 2: N-Queens Count
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * APPROACH: Backtracking with col/diag sets.
 * TIME:  O(n!)
 * SPACE: O(n)
 */

#include <iostream>
#include <set>
using namespace std;

int solve(int n) {
    int count = 0;
    set<int> cols, d1, d2;

    function<void(int)> backtrack = [&](int row) {
        if (row == n) { count++; return; }
        for (int col = 0; col < n; col++) {
            if (cols.count(col) || d1.count(row - col) || d2.count(row + col))
                continue;
            cols.insert(col);
            d1.insert(row - col);
            d2.insert(row + col);
            backtrack(row + 1);
            cols.erase(col);
            d1.erase(row - col);
            d2.erase(row + col);
        }
    };

    backtrack(0);
    return count;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
