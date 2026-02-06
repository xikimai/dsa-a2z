/*
 * Warmup 02: Rectangle Area
 * ==============================
 * Chapter 2: Your First Programs
 *
 * PROBLEM
 * -------
 * Given the length and width of a rectangle, compute its area.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing two space-separated integers: length and width.
 *
 * OUTPUT FORMAT
 * -------------
 * Print a single integer — the area of the rectangle.
 *
 * CONSTRAINTS
 * -----------
 * 1 <= length, width <= 10^4
 *
 * EXAMPLES
 * --------
 * Input:  5 3
 * Output: 15
 *
 * Input:  10 10
 * Output: 100
 *
 * Input:  1 1
 * Output: 1
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return 0;" in the solve() function with your solution.
 * The main function handles input/output — don't change it.
 */

#include <iostream>
using namespace std;

/**
 * Return the area of a rectangle with the given length and width.
 */
int solve(int length, int width) {
    // TODO: Replace this with your solution
    return 0;
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int length, width;
    cin >> length >> width;
    cout << solve(length, width) << endl;
    return 0;
}
