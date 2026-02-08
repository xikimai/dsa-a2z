/*
 * Challenge 2: Course Schedule
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Return true if all courses can be finished (no cycle).
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <vector>
using namespace std;

bool solve(int numCourses, vector<vector<int>>& prerequisites) {
    // TODO: Replace this with your solution
    return true;
}

int main() {
    int numCourses, m; cin >> numCourses >> m;
    vector<vector<int>> prereqs(m, vector<int>(2));
    for (int i = 0; i < m; i++) cin >> prereqs[i][0] >> prereqs[i][1];
    cout << (solve(numCourses, prereqs) ? "true" : "false") << endl;
    return 0;
}
