/*
 * Solution for Practice 03: Reverse Number
 * ==========================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Handle negative numbers by tracking the sign separately.
 * Then repeatedly extract the last digit (n % 10), append it to
 * the reversed number (reversed * 10 + digit), and remove
 * the last digit (n / 10).
 *
 * Leading zeros in the reversed result are naturally dropped
 * because we're building an integer, not a string.
 *
 * TIME COMPLEXITY:  O(d) — where d is the number of digits
 * SPACE COMPLEXITY: O(1) — just a few variables
 */

#include <iostream>
using namespace std;

int solve(int n) {
    int sign = 1;
    if (n < 0) {
        sign = -1;
        n = -n;
    }
    int reversed = 0;
    while (n > 0) {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    return sign * reversed;
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
