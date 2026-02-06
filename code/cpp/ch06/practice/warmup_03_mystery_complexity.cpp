/*
 * Warmup 3: Mystery Complexity
 * ============================
 * Chapter 6: How Fast Is Your Code?
 *
 * PROBLEM:
 *   You are given two parallel vectors: n_values and counts. For each
 *   n_values[i], counts[i] is the number of operations observed.
 *   Determine the Big-O complexity class that best fits the data.
 *
 *   Return one of: "O(1)", "O(log n)", "O(n)", or "O(n^2)".
 *
 * EXAMPLES:
 *   solve({1,10,100,1000}, {5,5,5,5})           -> "O(1)"
 *   solve({1,2,4,8,16}, {0,1,2,3,4})            -> "O(log n)"
 *   solve({100,200,400,800}, {100,200,400,800})  -> "O(n)"
 *   solve({10,20,40,80}, {100,400,1600,6400})    -> "O(n^2)"
 *
 * CONSTRAINTS:
 *   - At least 2 data points
 *   - n_values are positive and increasing
 *   - counts are non-negative
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

/**
 * Classifies the complexity based on observed (n, count) data points.
 */
string solve(vector<int> n_values, vector<int> counts) {
    // TODO: Replace this with your solution
    return "";
}

// -- Do not change anything below this line --------------------------
int main() {
    int k;
    cin >> k;
    vector<int> n_values(k), counts(k);
    for (int i = 0; i < k; i++) cin >> n_values[i];
    for (int i = 0; i < k; i++) cin >> counts[i];
    cout << solve(n_values, counts) << endl;
    return 0;
}
