/*
 * Warmup 5: Intersection of Two Arrays
 * ======================================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM:
 *   Given two arrays, return the sorted list of unique common elements.
 *
 * EXAMPLES:
 *   solve({1,2,2,1}, {2,2})       -> {2}
 *   solve({4,9,5}, {9,4,9,8,4})   -> {4,9}
 *   solve({1,2,3}, {4,5,6})       -> {}
 *   solve({}, {1,2})              -> {}
 *
 * CONSTRAINTS:
 *   - 0 <= a.size(), b.size() <= 10^5
 *
 * INSTRUCTIONS:
 *   Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

vector<int> solve(vector<int> a, vector<int> b) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n, m;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    cin >> m;
    vector<int> b(m);
    for (int i = 0; i < m; i++) cin >> b[i];
    vector<int> result = solve(a, b);
    for (int x : result) cout << x << " ";
    cout << endl;
    return 0;
}
