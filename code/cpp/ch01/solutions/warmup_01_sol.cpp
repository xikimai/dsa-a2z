/*
 * Solution for Warmup 01: Sum of Two Numbers
 * ============================================
 * Chapter 1: The Coder's Toolkit
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Simply return a + b. No tricks needed for this one — the goal is to
 * practice the workflow: read input, compute, print output.
 *
 * TIME COMPLEXITY:  O(1) — just one addition
 * SPACE COMPLEXITY: O(1) — no extra memory used
 */

#include <iostream>
using namespace std;

/**
 * Return the sum of a and b.
 */
int solve(int a, int b) {
    return a + b;
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int a, b;
    cin >> a >> b;
    cout << solve(a, b) << endl;
    return 0;
}
