/*
 * Solution for Warmup 03: Largest of Three
 * ==========================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Start by assuming the first number is the largest. Then compare with
 * the second and third, updating if we find a larger one.
 * You could also use nested if/else or the max() function.
 *
 * TIME COMPLEXITY:  O(1) — two comparisons
 * SPACE COMPLEXITY: O(1) — one extra variable
 */

#include <iostream>
using namespace std;

int solve(int a, int b, int c) {
    int largest = a;
    if (b > largest) largest = b;
    if (c > largest) largest = c;
    return largest;
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int a, b, c;
    cin >> a >> b >> c;
    cout << solve(a, b, c) << endl;
    return 0;
}
