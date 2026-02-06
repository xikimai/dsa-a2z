/*
 * Challenge 02: Prime Check
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * PROBLEM
 * -------
 * Given an integer n, determine whether it is a prime number.
 * A prime number is greater than 1 and has no divisors other than 1
 * and itself.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing an integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print "true" if n is prime, "false" otherwise.
 *
 * CONSTRAINTS
 * -----------
 * -10^9 <= n <= 10^9
 *
 * EXAMPLES
 * --------
 * Input:  2
 * Output: true
 *
 * Input:  4
 * Output: false
 *
 * Input:  17
 * Output: true
 *
 * Input:  1
 * Output: false
 *
 * Input:  -5
 * Output: false
 *
 * INSTRUCTIONS
 * ------------
 * Replace the body of solve() with your solution.
 * The main() function handles I/O -- don't change it.
 *
 * HINT: You only need to check divisors up to sqrt(n).
 */

#include <iostream>
#include <string>
using namespace std;

/**
 * Return true if n is prime, false otherwise.
 */
bool solve(int n) {
    // TODO: Replace this with your solution
    return false;
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int n;
    cin >> n;
    cout << (solve(n) ? "true" : "false") << endl;
    return 0;
}
