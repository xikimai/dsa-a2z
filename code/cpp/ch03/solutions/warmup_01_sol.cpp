/*
 * Solution for Warmup 01: Even or Odd
 * =====================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Use the modulo operator (%) to check if n is divisible by 2.
 * If n % 2 == 0, the number is even; otherwise it's odd.
 * This works for negative numbers too: -3 % 2 == -1 (not 0), so it's odd.
 *
 * TIME COMPLEXITY:  O(1) — single arithmetic operation
 * SPACE COMPLEXITY: O(1) — no extra memory
 */

#include <iostream>
#include <string>
using namespace std;

string solve(int n) {
    return (n % 2 == 0) ? "Even" : "Odd";
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
