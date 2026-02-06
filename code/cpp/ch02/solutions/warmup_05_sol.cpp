/*
 * Solution for Warmup 05: Last Digit
 * ====================================
 * Chapter 2: Your First Programs
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Take the absolute value first (to handle negative numbers), then use
 * modulo 10 to extract the last digit.
 *
 * Why abs() first? Because in C++, -123 % 10 gives -3, not 3!
 * The modulo operator preserves the sign of the dividend.
 *
 * TIME COMPLEXITY:  O(1) — two operations
 * SPACE COMPLEXITY: O(1) — no extra memory
 */

#include <iostream>
#include <cstdlib>  // for abs
using namespace std;

/**
 * Return the last digit of n (always non-negative).
 */
int solve(int n) {
    return abs(n) % 10;
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
