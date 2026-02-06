/*
 * Warmup 2: Is It Fast Enough?
 * ============================
 * Chapter 6: How Fast Is Your Code?
 *
 * PROBLEM:
 *   Given an input size n and a complexity string, determine whether
 *   an algorithm with that complexity would finish in time -- i.e.,
 *   whether the number of operations is strictly less than 10^8
 *   (100 million).
 *
 *   Complexity strings and their operation counts:
 *     "1"       -> 1
 *     "log_n"   -> log2(n)
 *     "n"       -> n
 *     "n_log_n" -> n * log2(n)
 *     "n^2"     -> n * n
 *     "n^3"     -> n * n * n
 *     "2^n"     -> 2^n  (if n > 30, return false immediately)
 *
 * EXAMPLES:
 *   solve(1000, "n^2")   -> true
 *   solve(100000, "n^2") -> false
 *
 * CONSTRAINTS:
 *   - 1 <= n <= 10^9
 *   - complexity is one of the seven valid strings
 */

#include <cmath>
#include <iostream>
#include <string>
using namespace std;

/**
 * Returns true if the algorithm finishes within 10^8 operations.
 */
bool solve(int n, string complexity) {
    // TODO: Replace this with your solution
    return false;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    string complexity;
    cin >> n >> complexity;
    cout << (solve(n, complexity) ? "true" : "false") << endl;
    return 0;
}
