/*
 * Warmup 4: Sum of 1 to N
 * =======================
 * Chapter 6: How Fast Is Your Code?
 *
 * PROBLEM:
 *   Compute the sum 1 + 2 + ... + n using three different methods and
 *   return all three results as a vector {loop, formula, nested}.
 *     - loop:   O(n) single loop accumulation
 *     - formula: O(1) using n*(n+1)/2
 *     - nested: O(n^2) nested loop (add 1 for each (i,j) where j <= i)
 *
 * EXAMPLES:
 *   solve(10)  -> {55, 55, 55}
 *   solve(0)   -> {0, 0, 0}
 *
 * CONSTRAINTS:
 *   - 0 <= n <= 1000 (small, since nested is O(n^2))
 */

#include <iostream>
#include <vector>
using namespace std;

/**
 * Returns {loop_sum, formula_sum, nested_sum} for 1 + 2 + ... + n.
 */
vector<int> solve(int n) {
    // TODO: Replace this with your solution
    return {0, 0, 0};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> result = solve(n);
    cout << result[0] << " " << result[1] << " " << result[2] << endl;
    return 0;
}
