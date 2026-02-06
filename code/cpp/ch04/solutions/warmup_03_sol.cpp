/*
 * Solution — Warmup 3: Min of Three
 * ==================================
 * Chapter 4: Functions
 *
 * APPROACH:
 *   Write a min_of_two helper that returns the smaller of two ints.
 *   Chain two calls: min_of_two(a, min_of_two(b, c)).
 *
 * TIME COMPLEXITY:  O(1)
 * SPACE COMPLEXITY: O(1)
 */

#include <iostream>
using namespace std;

int min_of_two(int a, int b) {
    if (a < b) return a;
    return b;
}

int solve(int a, int b, int c) {
    return min_of_two(a, min_of_two(b, c));
}

// -- Do not change anything below this line --------------------------
int main() {
    int a, b, c;
    cin >> a >> b >> c;
    cout << solve(a, b, c) << endl;
    return 0;
}
