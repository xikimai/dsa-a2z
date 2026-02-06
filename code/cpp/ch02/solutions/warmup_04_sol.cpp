/*
 * Solution for Warmup 04: Swap Two Numbers
 * ==========================================
 * Chapter 2: Your First Programs
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Return the two values in reversed order using a pair.
 * C++ pairs let you bundle two values together — great for returning
 * multiple values from a function.
 *
 * TIME COMPLEXITY:  O(1) — just creating a pair
 * SPACE COMPLEXITY: O(1) — one pair
 */

#include <iostream>
#include <utility>  // for pair
using namespace std;

/**
 * Return the two values swapped as a pair (b first, a second).
 */
pair<int, int> solve(int a, int b) {
    return {b, a};
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int a, b;
    cin >> a >> b;
    auto result = solve(a, b);
    cout << result.first << " " << result.second << endl;
    return 0;
}
