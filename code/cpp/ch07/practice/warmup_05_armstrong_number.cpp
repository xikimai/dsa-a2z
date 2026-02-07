/*
 * Warmup 5: Armstrong Number
 * ==========================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * PROBLEM:
 *   An Armstrong number (narcissistic number) is a number where the
 *   sum of each digit raised to the power of the total number of digits
 *   equals the number itself.
 *
 *   Example: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
 *
 *   Given n, return true if it is an Armstrong number.
 *   Negative numbers are NOT Armstrong numbers.
 *
 * EXAMPLES:
 *   solve(153) -> true
 *   solve(370) -> true
 *   solve(9474) -> true
 *   solve(100) -> false
 *   solve(1) -> true
 *   solve(0) -> true
 *
 * CONSTRAINTS:
 *   -10^18 <= n <= 10^18
 *
 * INSTRUCTIONS:
 *   Replace "return false;" with your solution.
 *   1. Count the digits.
 *   2. Sum each digit raised to that power.
 *   3. Compare sum to original.
 */

#include <cmath>
#include <iostream>
using namespace std;

bool solve(long long n) {
    // TODO: Replace this with your solution
    return false;
}

// -- Do not change anything below this line --------------------------
int main() {
    long long n;
    cin >> n;
    cout << (solve(n) ? "true" : "false") << endl;
    return 0;
}
