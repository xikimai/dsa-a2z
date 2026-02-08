/*
 * Practice 3: Rat in a Maze
 * ====================================
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * PROBLEM:
 *   Find all paths from (0,0) to (N-1,N-1) in a binary grid.
 *   1 = open, 0 = wall. Return sorted path strings (D/L/R/U).
 *
 * CONSTRAINTS:
 *   - 1 <= N <= 5
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> solve(vector<vector<int>> maze) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<vector<int>> maze(n, vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> maze[i][j];
    vector<string> result = solve(maze);
    for (auto& path : result) cout << path << endl;
    return 0;
}
