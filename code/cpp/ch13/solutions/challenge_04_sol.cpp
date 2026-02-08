/*
 * Solution for Challenge 4: Fence Painting
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * APPROACH: Sort by start, merge overlapping intervals, sum lengths.
 * TIME:  O(N log N)
 * SPACE: O(1)
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<vector<int>> fences) {
    if (fences.empty()) return 0;
    sort(fences.begin(), fences.end());
    int total = 0;
    int cs = fences[0][0], ce = fences[0][1];
    for (int i = 1; i < (int)fences.size(); i++) {
        if (fences[i][0] <= ce) {
            ce = max(ce, fences[i][1]);
        } else {
            total += ce - cs;
            cs = fences[i][0];
            ce = fences[i][1];
        }
    }
    total += ce - cs;
    return total;
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
