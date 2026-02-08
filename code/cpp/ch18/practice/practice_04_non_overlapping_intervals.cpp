/*
 * Practice 4: Non-overlapping Intervals
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Min intervals to remove so rest don't overlap.
 * EXAMPLES: solve({{1,2},{2,3},{3,4},{1,3}}) -> 1
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<vector<int>> intervals) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n; cin >> n;
    vector<vector<int>> intervals(n, vector<int>(2));
    for (int i = 0; i < n; i++) cin >> intervals[i][0] >> intervals[i][1];
    cout << solve(intervals) << endl;
    return 0;
}
