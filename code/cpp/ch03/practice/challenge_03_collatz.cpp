/*
 * Challenge 03: Collatz Sequence
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * PROBLEM
 * -------
 * Given a positive integer n, return the Collatz sequence starting from n.
 * The Collatz sequence follows these rules:
 *   - If the current number is 1, stop.
 *   - If the current number is even, divide it by 2.
 *   - If the current number is odd, multiply by 3 and add 1.
 * The sequence always includes the starting number and ends with 1.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing a positive integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the Collatz sequence, space-separated.
 *
 * CONSTRAINTS
 * -----------
 * 1 <= n <= 10^6
 *
 * EXAMPLES
 * --------
 * Input:  6
 * Output: 6 3 10 5 16 8 4 2 1
 *
 * Input:  1
 * Output: 1
 *
 * Input:  2
 * Output: 2 1
 *
 * INSTRUCTIONS
 * ------------
 * Replace the body of solve() with your solution.
 * The main() function handles I/O -- don't change it.
 */

#include <iostream>
#include <vector>
using namespace std;

/**
 * Return the Collatz sequence starting from n.
 */
vector<int> solve(int n) {
    // TODO: Replace this with your solution
    return {};
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int n;
    cin >> n;
    vector<int> result = solve(n);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
