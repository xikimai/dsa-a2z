/*
 * Practice 3: Modular Exponentiation
 * ===================================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * PROBLEM:
 *   Compute (base^exp) % mod using binary exponentiation.
 *   This is MUCH faster than multiplying base*base*...*base exp times.
 *
 * EXAMPLES:
 *   solve(2, 10, 1000000007) -> 1024
 *   solve(2, 20, 1000000007) -> 1048576
 *   solve(123456789, 0, 1000000007) -> 1
 *   solve(2, 100, 1000000007) -> 976371285
 *
 * CONSTRAINTS:
 *   1 <= base <= 10^9
 *   0 <= exp <= 10^18
 *   2 <= mod <= 10^9
 *
 * INSTRUCTIONS:
 *   Replace "return 0;" with your solution.
 *   Use binary exponentiation: square base repeatedly, multiply
 *   into result when the current bit of exp is 1.
 *   Remember to take mod at EVERY multiplication to avoid overflow.
 */

#include <iostream>
using namespace std;

long long solve(long long base, long long exp, long long mod) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    long long base, exp, mod;
    cin >> base >> exp >> mod;
    cout << solve(base, exp, mod) << endl;
    return 0;
}
