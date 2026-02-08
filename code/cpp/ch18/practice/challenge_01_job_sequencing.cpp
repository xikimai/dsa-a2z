/*
 * Challenge 1: Job Sequencing with Deadlines
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Maximize profit scheduling jobs with deadlines.
 * EXAMPLES: solve({{1,4,20},{2,1,10},{3,1,40},{4,1,30}}) -> {2, 60}
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

pair<int,int> solve(vector<vector<int>> jobs) {
    // TODO: Replace this with your solution
    return {0, 0};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n; cin >> n;
    vector<vector<int>> jobs(n, vector<int>(3));
    for (int i = 0; i < n; i++) cin >> jobs[i][0] >> jobs[i][1] >> jobs[i][2];
    auto [count, profit] = solve(jobs);
    cout << count << " " << profit << endl;
    return 0;
}
