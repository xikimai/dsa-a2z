/*
 * Warmup 2: Power
 * ===============
 * Chapter 4: Functions
 *
 * PROBLEM:
 *   Compute base raised to the power of exponent using a loop.
 *   Do NOT use pow() from <cmath>.
 *
 * EXAMPLES:
 *   solve(2, 10)  -> 1024
 *   solve(3, 0)   -> 1
 *   solve(5, 3)   -> 125
 *   solve(7, 1)   -> 7
 *
 * CONSTRAINTS:
 *   - exponent >= 0
 *   - Use long long to avoid overflow for large results
 */

#include <iostream>
using namespace std;

/**
 * Returns base^exponent computed with a loop.
 */
long long solve(int base, int exponent) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int base, exponent;
    cin >> base >> exponent;
    cout << solve(base, exponent) << endl;
    return 0;
}
