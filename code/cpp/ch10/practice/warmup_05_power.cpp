/*
 * Warmup 5: Power (Exponentiation)
 * ==================================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM:
 *   Given integers base and exp, compute base^exp recursively.
 *   base^0 = 1, and base^exp = base * base^(exp-1) for exp > 0.
 *
 * EXAMPLES:
 *   solve(2, 0)  -> 1
 *   solve(2, 10) -> 1024
 *   solve(3, 4)  -> 81
 *   solve(5, 3)  -> 125
 *
 * CONSTRAINTS:
 *   0 <= base <= 10
 *   0 <= exp <= 20
 *   Use long long to avoid overflow.
 *
 * INSTRUCTIONS:
 *   Replace the body with your recursive solution.
 */

#include <iostream>
using namespace std;

long long solve(int base, int exp) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int base, exp;
    cin >> base >> exp;
    cout << solve(base, exp) << endl;
    return 0;
}
