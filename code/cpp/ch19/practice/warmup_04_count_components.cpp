/*
 * Warmup 4: Count Connected Components
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Count connected components in an undirected graph.
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int solve(int n, vector<vector<int>>& edges) {
    // TODO: Replace this with your solution
    return 0;
}

int main() {
    int n, m; cin >> n >> m;
    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) cin >> edges[i][0] >> edges[i][1];
    cout << solve(n, edges) << endl;
    return 0;
}
