/*
 * Solution -- Practice 2: Sum of Digits
 * ========================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Take absolute value first. Base case: single digit returns itself.
 *           Otherwise: last digit (n%10) + solve(n/10).
 * TIME:  O(d) where d is number of digits
 * SPACE: O(d) call stack
 */

#include <iostream>
using namespace std;

int solve(int n) {
    if (n < 0) n = -n;
    if (n < 10) return n;
    return n % 10 + solve(n / 10);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
