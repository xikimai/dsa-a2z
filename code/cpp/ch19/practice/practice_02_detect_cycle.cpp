/*
 * Practice 2: Detect Cycle in Undirected Graph
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Return true if the undirected graph contains a cycle.
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <vector>
using namespace std;

bool solve(int n, vector<vector<int>>& edges) {
    // TODO: Replace this with your solution
    return false;
}

int main() {
    int n, m; cin >> n >> m;
    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) cin >> edges[i][0] >> edges[i][1];
    cout << (solve(n, edges) ? "true" : "false") << endl;
    return 0;
}
