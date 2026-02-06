/*
 * Solution for Practice 04: Right Triangle
 * ==========================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * For each row i (1-indexed), print (n - i) spaces followed by i stars.
 * Join rows with newlines. No trailing newline.
 *
 * TIME COMPLEXITY:  O(n^2) — nested iteration over rows and columns
 * SPACE COMPLEXITY: O(n^2) — for the output string
 */

#include <iostream>
#include <string>
using namespace std;

string solve(int n) {
    string result;
    for (int i = 1; i <= n; i++) {
        if (i > 1) result += "\n";
        result += string(n - i, ' ') + string(i, '*');
    }
    return result;
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
