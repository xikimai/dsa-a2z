/*
 * Practice 1: Shortest Path (Unweighted)
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Find shortest distances from source to all nodes. -1 if unreachable.
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<int> solve(int n, vector<vector<int>>& edges, int source) {
    // TODO: Replace this with your solution
    return vector<int>(n, -1);
}

int main() {
    int n, m, source; cin >> n >> m >> source;
    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) cin >> edges[i][0] >> edges[i][1];
    auto dist = solve(n, edges, source);
    for (int i = 0; i < n; i++) cout << dist[i] << " ";
    cout << endl;
    return 0;
}
