/*
 * Solution for Warmup 02: Rectangle Area
 * ========================================
 * Chapter 2: Your First Programs
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Multiply length by width. That's it!
 *
 * TIME COMPLEXITY:  O(1) — single multiplication
 * SPACE COMPLEXITY: O(1) — no extra memory
 */

#include <iostream>
using namespace std;

/**
 * Return the area of a rectangle with the given length and width.
 */
int solve(int length, int width) {
    return length * width;
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int length, width;
    cin >> length >> width;
    cout << solve(length, width) << endl;
    return 0;
}
