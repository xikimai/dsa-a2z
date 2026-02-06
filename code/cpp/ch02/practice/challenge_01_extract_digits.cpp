/*
 * Challenge 01: Extract Digits
 * ==============================
 * Chapter 2: Your First Programs
 *
 * PROBLEM
 * -------
 * Given a 3-digit integer, extract its hundreds, tens, and ones digits.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing an integer n (a 3-digit number).
 *
 * OUTPUT FORMAT
 * -------------
 * Print three integers separated by spaces: hundreds tens ones
 *
 * CONSTRAINTS
 * -----------
 * 100 <= n <= 999
 *
 * EXAMPLES
 * --------
 * Input:  123
 * Output: 1 2 3
 *
 * Input:  905
 * Output: 9 0 5
 *
 * Input:  100
 * Output: 1 0 0
 *
 * Input:  999
 * Output: 9 9 9
 *
 * INSTRUCTIONS
 * ------------
 * Fill in the solve() function using integer division (/) and modulo (%).
 * Hint: hundreds = n / 100, tens = (n / 10) % 10, ones = n % 10
 * The main function handles input/output — don't change it.
 */

#include <iostream>
#include <tuple>  // for tuple
using namespace std;

/**
 * Extract the hundreds, tens, and ones digits of a 3-digit number.
 * Returns a tuple of (hundreds, tens, ones).
 */
tuple<int, int, int> solve(int n) {
    // TODO: Replace this with your solution
    return {0, 0, 0};
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int n;
    cin >> n;
    auto [h, t, o] = solve(n);
    cout << h << " " << t << " " << o << endl;
    return 0;
}
