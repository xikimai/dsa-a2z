/*
 * Warmup 5: Is Path Exists
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Check if a path exists between source and dest.
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

bool solve(int n, vector<vector<int>>& edges, int source, int dest) {
    // TODO: Replace this with your solution
    return false;
}

int main() {
    int n, m, source, dest; cin >> n >> m >> source >> dest;
    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) cin >> edges[i][0] >> edges[i][1];
    cout << (solve(n, edges, source, dest) ? "true" : "false") << endl;
    return 0;
}
