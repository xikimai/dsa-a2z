/*
 * Practice 03: Distance Between Two Points
 * ==========================================
 * Chapter 2: Your First Programs
 *
 * PROBLEM
 * -------
 * Given two points (x1, y1) and (x2, y2) on a 2D plane, compute the
 * Euclidean distance between them.
 * Formula: distance = sqrt((x2-x1)^2 + (y2-y1)^2)
 *
 * INPUT FORMAT
 * ------------
 * A single line containing four space-separated doubles: x1 y1 x2 y2
 *
 * OUTPUT FORMAT
 * -------------
 * Print a single double — the distance between the two points.
 *
 * CONSTRAINTS
 * -----------
 * -10^4 <= x1, y1, x2, y2 <= 10^4
 *
 * EXAMPLES
 * --------
 * Input:  0 0 3 4
 * Output: 5
 *
 * Input:  1 1 1 1
 * Output: 0
 *
 * Input:  0 0 1 1
 * Output: 1.41421  (approximately)
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return 0.0;" in the solve() function with your solution.
 * Use sqrt() and pow() from <cmath>, or just multiply manually.
 * The main function handles input/output — don't change it.
 */

#include <iostream>
#include <cmath>  // for sqrt
using namespace std;

/**
 * Return the Euclidean distance between points (x1,y1) and (x2,y2).
 */
double solve(double x1, double y1, double x2, double y2) {
    // TODO: Replace this with your solution
    return 0.0;
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    double x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    cout << solve(x1, y1, x2, y2) << endl;
    return 0;
}
