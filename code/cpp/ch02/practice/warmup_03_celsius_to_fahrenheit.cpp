/*
 * Warmup 03: Celsius to Fahrenheit
 * ==================================
 * Chapter 2: Your First Programs
 *
 * PROBLEM
 * -------
 * Convert a temperature from Celsius to Fahrenheit.
 * Formula: F = C * 9.0 / 5.0 + 32.0
 *
 * INPUT FORMAT
 * ------------
 * A single line containing a double: the temperature in Celsius.
 *
 * OUTPUT FORMAT
 * -------------
 * Print a single double — the temperature in Fahrenheit.
 *
 * CONSTRAINTS
 * -----------
 * -273.15 <= celsius <= 10^6
 *
 * EXAMPLES
 * --------
 * Input:  0
 * Output: 32
 *
 * Input:  100
 * Output: 212
 *
 * Input:  -40
 * Output: -40
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return 0.0;" in the solve() function with your solution.
 * The main function handles input/output — don't change it.
 */

#include <iostream>
using namespace std;

/**
 * Convert celsius to fahrenheit and return the result.
 */
double solve(double celsius) {
    // TODO: Replace this with your solution
    return 0.0;
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    double celsius;
    cin >> celsius;
    cout << solve(celsius) << endl;
    return 0;
}
