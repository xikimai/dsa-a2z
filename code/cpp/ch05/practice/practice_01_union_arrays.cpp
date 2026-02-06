/*
 * Practice 1: Union of Two Arrays
 * ================================
 * Chapter 5: Collections
 *
 * PROBLEM:
 *   Given two vectors of integers, return their sorted union
 *   (all unique elements from both, in ascending order).
 *
 * EXAMPLES:
 *   solve({1, 2, 3}, {3, 4, 5}) -> {1, 2, 3, 4, 5}
 *   solve({1, 1, 2}, {2, 3})    -> {1, 2, 3}
 *   solve({}, {1, 2})           -> {1, 2}
 *
 * CONSTRAINTS:
 *   - 0 <= a.size(), b.size() <= 10^5
 */

#include <iostream>
#include <vector>
using namespace std;

/**
 * Returns the sorted union of a and b (unique elements only).
 */
vector<int> solve(vector<int>& a, vector<int>& b) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int m;
    cin >> m;
    vector<int> b(m);
    for (int i = 0; i < m; i++) cin >> b[i];
    vector<int> result = solve(a, b);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
