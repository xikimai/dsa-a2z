/*
 * Solution — Warmup 2: Power
 * ==========================
 * Chapter 4: Functions
 *
 * APPROACH:
 *   Multiply base by itself 'exponent' times using a loop.
 *   Start with result = 1 (since anything^0 = 1).
 *
 * TIME COMPLEXITY:  O(exponent)
 * SPACE COMPLEXITY: O(1)
 */

#include <iostream>
using namespace std;

long long solve(int base, int exponent) {
    long long result = 1;
    for (int i = 0; i < exponent; i++) {
        result *= base;
    }
    return result;
}

// -- Do not change anything below this line --------------------------
int main() {
    int base, exponent;
    cin >> base >> exponent;
    cout << solve(base, exponent) << endl;
    return 0;
}
