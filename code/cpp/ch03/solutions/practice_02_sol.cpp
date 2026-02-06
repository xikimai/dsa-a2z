/*
 * Solution for Practice 02: Digit Count
 * =======================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Handle special case: if n is 0, return 1.
 * Otherwise, make n positive (handle negative), then repeatedly
 * divide by 10 and count how many times until n becomes 0.
 *
 * TIME COMPLEXITY:  O(d) — where d is the number of digits
 * SPACE COMPLEXITY: O(1) — just a counter
 */

#include <iostream>
using namespace std;

int solve(int n) {
    if (n == 0) return 1;
    if (n < 0) n = -n;
    int count = 0;
    while (n > 0) {
        n /= 10;
        count++;
    }
    return count;
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
