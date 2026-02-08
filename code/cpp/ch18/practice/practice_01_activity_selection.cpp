/*
 * Practice 1: Activity Selection
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Max non-overlapping activities.
 * EXAMPLES: solve({{1,2},{3,4},{0,6},{5,7},{8,9},{5,9}}) -> 4
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<vector<int>> activities) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n; cin >> n;
    vector<vector<int>> activities(n, vector<int>(2));
    for (int i = 0; i < n; i++) cin >> activities[i][0] >> activities[i][1];
    cout << solve(activities) << endl;
    return 0;
}
