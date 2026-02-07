/*
 * Warmup 5: Sort by Absolute Value
 * =================================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * PROBLEM:
 *   Sort the array by absolute value in ascending order.
 *   When two elements have the same absolute value, maintain their
 *   relative order (stable sort) or place the smaller value first.
 *
 * EXAMPLES:
 *   solve({3,-1,2,-5,4})   -> {-1,2,3,4,-5}
 *   solve({-10,7,-3,1})    -> {1,-3,7,-10}
 *   solve({0,-5,3,-1,8})   -> {0,-1,3,-5,8}
 *   solve({1,2,3})         -> {1,2,3}
 *   solve({-1})            -> {-1}
 *
 * CONSTRAINTS:
 *   0 <= arr.size() <= 10^5
 *   -10^6 <= arr[i] <= 10^6
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution.
 *   Hint: Use sort() with a custom comparator.
 */

#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr) {
    // TODO: Replace this with your solution
    return arr;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<int> result = solve(arr);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
