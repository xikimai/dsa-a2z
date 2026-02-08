/*
 * Solution -- Warmup 5: Power (Exponentiation)
 * ================================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Base case exp==0 returns 1.
 *           Otherwise base * solve(base, exp-1).
 * TIME:  O(exp)
 * SPACE: O(exp) call stack
 */

#include <iostream>
using namespace std;

long long solve(int base, int exp) {
    if (exp == 0) return 1;
    return (long long)base * solve(base, exp - 1);
}

// -- Do not change anything below this line --------------------------
int main() {
    int base, exp;
    cin >> base >> exp;
    cout << solve(base, exp) << endl;
    return 0;
}
