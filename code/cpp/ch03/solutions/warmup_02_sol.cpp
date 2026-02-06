/*
 * Solution for Warmup 02: Absolute Value
 * ========================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * If n is negative, return -n (which flips the sign to positive).
 * Otherwise, return n as-is.
 *
 * TIME COMPLEXITY:  O(1) — one comparison and possibly one negation
 * SPACE COMPLEXITY: O(1) — no extra memory
 */

#include <iostream>
using namespace std;

int solve(int n) {
    if (n < 0) return -n;
    return n;
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
