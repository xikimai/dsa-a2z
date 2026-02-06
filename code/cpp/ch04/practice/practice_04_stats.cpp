/*
 * Practice 4: Statistics
 * ======================
 * Chapter 4: Functions
 *
 * PROBLEM:
 *   Compute basic statistics for a vector of integers.
 *   Write helper functions: find_min, find_max, find_average.
 *   Do NOT use built-in min/max functions.
 *   Return results as a vector<double> with {min, max, average}.
 *   Average should be rounded to 2 decimal places.
 *
 * EXAMPLES:
 *   solve({1, 2, 3, 4, 5})   -> {1.0, 5.0, 3.0}
 *   solve({10})               -> {10.0, 10.0, 10.0}
 *   solve({-3, 0, 3})        -> {-3.0, 3.0, 0.0}
 *   solve({7, 7, 7})         -> {7.0, 7.0, 7.0}
 *
 * CONSTRAINTS:
 *   - nums is non-empty (at least 1 element)
 *   - Round average to 2 decimal places: round(avg * 100.0) / 100.0
 *   - Return empty vector for empty input
 */

#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

// TODO: Write helpers: find_min, find_max, find_average

/**
 * Returns {min, max, average} of the input vector.
 */
vector<double> solve(vector<int> nums) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    vector<double> result = solve(nums);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
