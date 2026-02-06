/*
 * Warmup 06: Multiplication Table
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * PROBLEM
 * -------
 * Given a positive integer n, return a vector of 10 strings representing
 * the multiplication table for n, from 1 x n to 10 x n.
 * Each string should be formatted as: "i x n = result"
 *
 * INPUT FORMAT
 * ------------
 * A single line containing a positive integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print 10 lines, each in the format "i x n = result".
 *
 * CONSTRAINTS
 * -----------
 * 1 <= n <= 1000
 *
 * EXAMPLES
 * --------
 * Input:  7
 * Output:
 *   1 x 7 = 7
 *   2 x 7 = 14
 *   3 x 7 = 21
 *   ...
 *   10 x 7 = 70
 *
 * INSTRUCTIONS
 * ------------
 * Replace the body of solve() with your solution.
 * The main() function handles I/O -- don't change it.
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

/**
 * Return a vector of 10 strings for the multiplication table of n.
 * Format: "i x n = result" for i = 1..10.
 */
vector<string> solve(int n) {
    // TODO: Replace this with your solution
    return {};
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int n;
    cin >> n;
    vector<string> result = solve(n);
    for (const string& line : result) {
        cout << line << endl;
    }
    return 0;
}
