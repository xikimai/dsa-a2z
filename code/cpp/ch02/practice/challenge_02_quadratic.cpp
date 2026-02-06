/*
 * Challenge 02: Quadratic Discriminant
 * ======================================
 * Chapter 2: Your First Programs
 *
 * PROBLEM
 * -------
 * Given the coefficients a, b, c of a quadratic equation ax^2 + bx + c = 0,
 * compute the discriminant and determine how many real roots exist.
 *
 * Discriminant = b^2 - 4ac
 *   - If discriminant > 0: 2 real roots
 *   - If discriminant == 0: 1 real root (a repeated root)
 *   - If discriminant < 0: 0 real roots
 *
 * INPUT FORMAT
 * ------------
 * A single line containing three space-separated doubles: a b c
 *
 * OUTPUT FORMAT
 * -------------
 * Print two values separated by a space: the discriminant and the
 * number of real roots.
 *
 * CONSTRAINTS
 * -----------
 * -10^3 <= a, b, c <= 10^3
 * a != 0
 *
 * EXAMPLES
 * --------
 * Input:  1 -3 2
 * Output: 1 2
 *   (disc = 9 - 8 = 1, which is > 0 so 2 roots)
 *
 * Input:  1 2 1
 * Output: 0 1
 *   (disc = 4 - 4 = 0, so 1 root)
 *
 * Input:  1 0 1
 * Output: -4 0
 *   (disc = 0 - 4 = -4, which is < 0 so 0 roots)
 *
 * INSTRUCTIONS
 * ------------
 * Fill in the solve() function. Return the discriminant and root count as a pair.
 * The main function handles input/output — don't change it.
 */

#include <iostream>
#include <utility>  // for pair
using namespace std;

/**
 * Compute the discriminant and number of real roots.
 * Returns a pair of (discriminant, number_of_roots).
 */
pair<double, int> solve(double a, double b, double c) {
    // TODO: Replace this with your solution
    return {0.0, 0};
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    double a, b, c;
    cin >> a >> b >> c;
    auto [disc, numRoots] = solve(a, b, c);
    cout << disc << " " << numRoots << endl;
    return 0;
}
