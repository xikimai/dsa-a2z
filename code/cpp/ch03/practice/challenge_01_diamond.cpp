/*
 * Challenge 01: Diamond Pattern
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * PROBLEM
 * -------
 * Given a positive integer n, return a string representing a diamond
 * pattern made of stars. The diamond has n rows in the top half
 * (including the middle/widest row) and n-1 rows in the bottom half.
 * Total rows = 2*n - 1. The widest row has 2*n - 1 stars.
 *
 * For n = 1:
 *   *
 *
 * For n = 2:
 *    *
 *   ***
 *    *
 *
 * For n = 3:
 *     *
 *    ***
 *   *****
 *    ***
 *     *
 *
 * Lines are separated by newlines. No trailing newline.
 * No trailing spaces on any line.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing a positive integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the diamond pattern.
 *
 * CONSTRAINTS
 * -----------
 * 1 <= n <= 25
 *
 * EXAMPLES
 * --------
 * Input:  1
 * Output: *
 *
 * Input:  2
 * Output:
 *  *
 * ***
 *  *
 *
 * INSTRUCTIONS
 * ------------
 * Replace the body of solve() with your solution.
 * The main() function handles I/O -- don't change it.
 */

#include <iostream>
#include <string>
using namespace std;

/**
 * Return a diamond pattern string with n as the half-height (including center).
 * Rows separated by '\n'. No trailing newline or trailing spaces.
 */
string solve(int n) {
    // TODO: Replace this with your solution
    return "";
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
