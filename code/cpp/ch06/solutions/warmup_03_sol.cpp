/*
 * Solution -- Warmup 3: Mystery Complexity
 * =========================================
 * Chapter 6: How Fast Is Your Code?
 *
 * APPROACH:
 *   Look at how the count changes as n doubles (or grows).
 *   Compare ratios of consecutive counts and n values:
 *     - O(1):      counts stay roughly constant
 *     - O(log n):  counts grow by a constant additive amount when n doubles
 *     - O(n):      count ratio ~ n ratio (linear growth)
 *     - O(n^2):    count ratio ~ (n ratio)^2 (quadratic growth)
 *
 *   We use the ratio of the last two data points for classification.
 *
 * TIME COMPLEXITY:  O(k) where k is the number of data points
 * SPACE COMPLEXITY: O(1)
 */

#include <cmath>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string solve(vector<int> n_values, vector<int> counts) {
    int k = (int)n_values.size();

    // Check if all counts are the same -> O(1)
    bool all_same = true;
    for (int i = 1; i < k; i++) {
        if (counts[i] != counts[0]) {
            all_same = false;
            break;
        }
    }
    if (all_same) return "O(1)";

    // Look at ratio of counts vs ratio of n values (last two points)
    double n_ratio = (double)n_values[k - 1] / n_values[k - 2];
    double c_ratio = (double)counts[k - 1] / counts[k - 2];

    // O(n^2): count ratio ~ n_ratio^2
    if (abs(c_ratio - n_ratio * n_ratio) < 0.5) return "O(n^2)";

    // O(n): count ratio ~ n_ratio
    if (abs(c_ratio - n_ratio) < 0.5) return "O(n)";

    // O(log n): counts grow slowly (additively when n doubles)
    return "O(log n)";
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
