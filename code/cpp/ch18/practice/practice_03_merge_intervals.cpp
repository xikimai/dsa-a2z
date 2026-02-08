/*
 * Practice 3: Merge Intervals
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Merge overlapping intervals.
 * EXAMPLES: solve({{1,3},{2,6},{8,10},{15,18}}) -> {{1,6},{8,10},{15,18}}
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> solve(vector<vector<int>> intervals) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n; cin >> n;
    vector<vector<int>> intervals(n, vector<int>(2));
    for (int i = 0; i < n; i++) cin >> intervals[i][0] >> intervals[i][1];
    auto result = solve(intervals);
    for (auto& r : result) cout << r[0] << " " << r[1] << endl;
    return 0;
}
