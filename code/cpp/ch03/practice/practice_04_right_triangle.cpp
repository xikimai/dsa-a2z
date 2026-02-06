/*
 * Practice 04: Right Triangle
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * PROBLEM
 * -------
 * Given a positive integer n, return a string representing a right-aligned
 * right triangle of stars with n rows.
 *
 * For n = 3:
 *     *
 *    **
 *   ***
 *
 * For n = 4:
 *      *
 *     **
 *    ***
 *   ****
 *
 * Lines are separated by newlines. There is NO trailing newline.
 * Each row has leading spaces so the stars are right-aligned.
 * No trailing spaces on any line.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing a positive integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the right-aligned triangle pattern.
 *
 * CONSTRAINTS
 * -----------
 * 1 <= n <= 50
 *
 * EXAMPLES
 * --------
 * Input:  1
 * Output: *
 *
 * Input:  3
 * Output:
 *   *
 *  **
 * ***
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
 * Return a string with a right-aligned right triangle of n rows.
 * Rows are separated by '\n'. No trailing newline.
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
