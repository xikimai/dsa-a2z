/*
 * Solution for Challenge 02: Quadratic Discriminant
 * ===================================================
 * Chapter 2: Your First Programs
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * 1. Compute discriminant = b*b - 4*a*c
 * 2. Count real roots based on the sign of the discriminant:
 *    - disc > 0  => 2 distinct real roots
 *    - disc == 0 => 1 repeated real root
 *    - disc < 0  => 0 real roots (roots are complex)
 *
 * This connects algebra to programming — the discriminant tells you
 * everything about a quadratic equation's solutions!
 *
 * TIME COMPLEXITY:  O(1) — a few arithmetic operations
 * SPACE COMPLEXITY: O(1) — no extra memory
 */

#include <iostream>
#include <utility>  // for pair
using namespace std;

/**
 * Compute the discriminant and number of real roots.
 * Returns a pair of (discriminant, number_of_roots).
 */
pair<double, int> solve(double a, double b, double c) {
    double disc = b * b - 4.0 * a * c;
    int numRoots;
    if (disc > 0) {
        numRoots = 2;
    } else if (disc == 0) {
        numRoots = 1;
    } else {
        numRoots = 0;
    }
    return {disc, numRoots};
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    double a, b, c;
    cin >> a >> b >> c;
    auto [disc, numRoots] = solve(a, b, c);
    cout << disc << " " << numRoots << endl;
    return 0;
}
