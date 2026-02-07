/*
 * Practice 5: Trailing Zeros in Factorial
 * ========================================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * PROBLEM:
 *   Given a non-negative integer n, return the number of trailing
 *   zeros in n! (n factorial).
 *
 *   Trailing zeros come from factors of 10 = 2 * 5.
 *   Since there are always more 2s than 5s, count the 5s!
 *
 * EXAMPLES:
 *   solve(5)   -> 1    (5! = 120 -> one trailing zero)
 *   solve(10)  -> 2    (10! = 3628800)
 *   solve(25)  -> 6    (25 contributes an extra 5: 5, 10, 15, 20, 25)
 *   solve(100) -> 24
 *   solve(0)   -> 0
 *
 * CONSTRAINTS:
 *   0 <= n <= 10^9
 *
 * INSTRUCTIONS:
 *   Replace "return 0;" with your solution.
 *   Hint: count = n/5 + n/25 + n/125 + n/625 + ...
 */

#include <iostream>
using namespace std;

int solve(int n) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
