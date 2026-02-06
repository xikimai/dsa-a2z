/*
 * Practice 02: Time Conversion
 * ===============================
 * Chapter 2: Your First Programs
 *
 * PROBLEM
 * -------
 * Given a total number of seconds, convert it to hours, minutes, and seconds.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing an integer: the total number of seconds.
 *
 * OUTPUT FORMAT
 * -------------
 * Print three integers separated by colons: hours:minutes:seconds
 *
 * CONSTRAINTS
 * -----------
 * 0 <= totalSeconds <= 10^6
 *
 * EXAMPLES
 * --------
 * Input:  3661
 * Output: 1:1:1
 *
 * Input:  0
 * Output: 0:0:0
 *
 * Input:  7200
 * Output: 2:0:0
 *
 * Input:  90
 * Output: 0:1:30
 *
 * INSTRUCTIONS
 * ------------
 * Fill in the solve() function to break total seconds into h, m, s.
 * Hint: Use integer division (/) and modulo (%).
 * The main function handles input/output — don't change it.
 */

#include <iostream>
#include <tuple>  // for tuple
using namespace std;

/**
 * Convert totalSeconds into hours, minutes, and seconds.
 * Returns a tuple of (hours, minutes, seconds).
 */
tuple<int, int, int> solve(int totalSeconds) {
    // TODO: Replace this with your solution
    return {0, 0, 0};
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int totalSeconds;
    cin >> totalSeconds;
    auto [h, m, s] = solve(totalSeconds);
    cout << h << ":" << m << ":" << s << endl;
    return 0;
}
