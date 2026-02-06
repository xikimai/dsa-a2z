/*
 * Warmup 05: Last Digit
 * ==============================
 * Chapter 2: Your First Programs
 *
 * PROBLEM
 * -------
 * Given an integer, return its last digit. The result should always
 * be non-negative (e.g., the last digit of -123 is 3, not -3).
 *
 * INPUT FORMAT
 * ------------
 * A single line containing an integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print a single integer — the last digit of n.
 *
 * CONSTRAINTS
 * -----------
 * -10^9 <= n <= 10^9
 *
 * EXAMPLES
 * --------
 * Input:  123
 * Output: 3
 *
 * Input:  -456
 * Output: 6
 *
 * Input:  0
 * Output: 0
 *
 * Input:  10
 * Output: 0
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return 0;" in the solve() function with your solution.
 * Hint: Use abs() to handle negative numbers, then use % 10.
 * The main function handles input/output — don't change it.
 */

#include <iostream>
#include <cstdlib>  // for abs
using namespace std;

/**
 * Return the last digit of n (always non-negative).
 */
int solve(int n) {
    // TODO: Replace this with your solution
    return 0;
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
