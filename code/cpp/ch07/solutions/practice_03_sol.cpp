/*
 * Solution -- Practice 3: Modular Exponentiation
 * ================================================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * APPROACH: Binary exponentiation. Square the base repeatedly and multiply
 *           into result when the current bit of exp is 1. Take mod at every
 *           multiplication step.
 * TIME:  O(log(exp))
 * SPACE: O(1)
 */

#include <iostream>
using namespace std;

long long solve(long long base, long long exp, long long mod) {
    long long result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = result * base % mod;
        }
        exp /= 2;
        base = base * base % mod;
    }
    return result;
}

// -- Do not change anything below this line --------------------------
int main() {
    long long base, exp, mod;
    cin >> base >> exp >> mod;
    cout << solve(base, exp, mod) << endl;
    return 0;
}
