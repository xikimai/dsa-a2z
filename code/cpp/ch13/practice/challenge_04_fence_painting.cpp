/*
 * Challenge 4: Fence Painting (USACO Bronze Style)
 * ====================================
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * PROBLEM:
 *   Given fence segments as {start, end} intervals, compute the
 *   total painted length with no double-counting.
 *
 * EXAMPLES:
 *   solve({{0,5},{3,8}})  -> 8
 *   solve({{1,3},{5,7}})  -> 4
 *   solve({})              -> 0
 *
 * CONSTRAINTS:
 *   - 0 <= fences.size() <= 10^4
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<vector<int>> fences) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<vector<int>> fences(n, vector<int>(2));
    for (int i = 0; i < n; i++) cin >> fences[i][0] >> fences[i][1];
    cout << solve(fences) << endl;
    return 0;
}
