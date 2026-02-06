/*
 * Warmup 04: Swap Two Numbers
 * ==============================
 * Chapter 2: Your First Programs
 *
 * PROBLEM
 * -------
 * Given two integers, return them in swapped order.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing two space-separated integers: a and b.
 *
 * OUTPUT FORMAT
 * -------------
 * Print two integers, b then a, separated by a space.
 *
 * CONSTRAINTS
 * -----------
 * -10^6 <= a, b <= 10^6
 *
 * EXAMPLES
 * --------
 * Input:  3 7
 * Output: 7 3
 *
 * Input:  0 0
 * Output: 0 0
 *
 * Input:  -1 5
 * Output: 5 -1
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return {0, 0};" in the solve() function with your solution.
 * The main function handles input/output — don't change it.
 */

#include <iostream>
#include <utility>  // for pair
using namespace std;

/**
 * Return the two values swapped as a pair (b first, a second).
 */
pair<int, int> solve(int a, int b) {
    // TODO: Replace this with your solution
    return {0, 0};
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int a, b;
    cin >> a >> b;
    auto result = solve(a, b);
    cout << result.first << " " << result.second << endl;
    return 0;
}
