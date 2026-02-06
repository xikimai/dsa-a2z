/*
 * Challenge 2: Performance Showdown
 * ==================================
 * Chapter 6: How Fast Is Your Code?
 *
 * PROBLEM:
 *   Given two complexity strings and an input size n, determine which
 *   algorithm is faster (fewer operations).
 *
 *   Complexity strings and their operation counts:
 *     "1"       -> 1
 *     "log_n"   -> log2(n)
 *     "n"       -> n
 *     "n_log_n" -> n * log2(n)
 *     "n^2"     -> n * n
 *     "n^3"     -> n * n * n
 *     "2^n"     -> 2^n
 *
 *   Return "A" if A is faster, "B" if B is faster, "TIE" if equal.
 *
 * EXAMPLES:
 *   solve("n^2", "n_log_n", 1000) -> "B"
 *   solve("n", "n", 100)          -> "TIE"
 *   solve("1", "log_n", 1000000)  -> "A"
 *
 * CONSTRAINTS:
 *   - 1 <= n <= 10^9
 *   - complexity_a and complexity_b are valid complexity strings
 */

#include <cmath>
#include <iostream>
#include <string>
using namespace std;

/**
 * Returns "A", "B", or "TIE" based on which complexity is faster at size n.
 */
string solve(string complexity_a, string complexity_b, int n) {
    // TODO: Replace this with your solution
    return "";
}

// -- Do not change anything below this line --------------------------
int main() {
    string a, b;
    int n;
    cin >> a >> b >> n;
    cout << solve(a, b, n) << endl;
    return 0;
}
