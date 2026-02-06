/*
 * Solution for Warmup 03: Celsius to Fahrenheit
 * ===============================================
 * Chapter 2: Your First Programs
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Apply the formula F = C * 9.0 / 5.0 + 32.0
 * Important: Use 9.0 and 5.0 (not 9 and 5) to get double division,
 * not integer division!
 *
 * TIME COMPLEXITY:  O(1) — a few arithmetic operations
 * SPACE COMPLEXITY: O(1) — no extra memory
 */

#include <iostream>
using namespace std;

/**
 * Convert celsius to fahrenheit and return the result.
 */
double solve(double celsius) {
    return celsius * 9.0 / 5.0 + 32.0;
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    double celsius;
    cin >> celsius;
    cout << solve(celsius) << endl;
    return 0;
}
