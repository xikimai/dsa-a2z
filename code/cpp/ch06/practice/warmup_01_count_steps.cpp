/*
 * Warmup 1: Count the Steps
 * =========================
 * Chapter 6: How Fast Is Your Code?
 *
 * PROBLEM:
 *   Given a code_id string and an integer n, return the exact number
 *   of operations that the corresponding code pattern would perform.
 *
 *   The code patterns are:
 *     "single_loop"    -> n              (one loop from 1 to n)
 *     "double_loop"    -> n * n          (two nested loops, each 1 to n)
 *     "half_loop"      -> n / 2          (loop that skips every other)
 *     "dependent_loop" -> n*(n+1) / 2    (inner loop depends on outer)
 *     "log_loop"       -> floor(log2(n)) (halving loop), 0 if n < 1
 *
 * EXAMPLES:
 *   solve("single_loop", 100) -> 100
 *   solve("double_loop", 10)  -> 100
 *   solve("log_loop", 16)     -> 4
 *
 * CONSTRAINTS:
 *   - 0 <= n <= 10^9
 *   - code_id is always one of the five valid strings
 */

#include <cmath>
#include <iostream>
#include <string>
using namespace std;

/**
 * Returns the exact operation count for the given code pattern and n.
 */
int solve(string code_id, int n) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    string code_id;
    int n;
    cin >> code_id >> n;
    cout << solve(code_id, n) << endl;
    return 0;
}
