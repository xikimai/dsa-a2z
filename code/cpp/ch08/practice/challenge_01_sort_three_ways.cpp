/*
 * Challenge 1: Sort Three Ways
 * ==============================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * PROBLEM:
 *   Implement three different sorting approaches for the same input:
 *
 *   1. solve_bubble(arr) -- Bubble sort
 *   2. solve_merge(arr)  -- Merge sort
 *   3. solve_builtin(arr) -- C++ std::sort
 *
 *   solve(arr) should call solve_merge(arr).
 *
 *   All three must produce the same sorted output.
 *
 * EXAMPLES:
 *   solve_bubble({5,3,8,1,2})  -> {1,2,3,5,8}
 *   solve_merge({5,3,8,1,2})   -> {1,2,3,5,8}
 *   solve_builtin({5,3,8,1,2}) -> {1,2,3,5,8}
 *
 * CONSTRAINTS:
 *   0 <= arr.size() <= 10^4
 *   -10^6 <= arr[i] <= 10^6
 *
 * INSTRUCTIONS:
 *   Replace each function body with your solution.
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve_bubble(vector<int> arr) {
    // TODO: Replace this with your solution
    return arr;
}

vector<int> solve_merge(vector<int> arr) {
    // TODO: Replace this with your solution
    return arr;
}

vector<int> solve_builtin(vector<int> arr) {
    // TODO: Replace this with your solution
    return arr;
}

vector<int> solve(vector<int> arr) {
    return solve_merge(arr);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    vector<int> r1 = solve_bubble(arr);
    vector<int> r2 = solve_merge(arr);
    vector<int> r3 = solve_builtin(arr);

    cout << "bubble:  ";
    for (int i = 0; i < (int)r1.size(); i++) { if (i > 0) cout << " "; cout << r1[i]; }
    cout << endl;

    cout << "merge:   ";
    for (int i = 0; i < (int)r2.size(); i++) { if (i > 0) cout << " "; cout << r2[i]; }
    cout << endl;

    cout << "builtin: ";
    for (int i = 0; i < (int)r3.size(); i++) { if (i > 0) cout << " "; cout << r3[i]; }
    cout << endl;
    return 0;
}
