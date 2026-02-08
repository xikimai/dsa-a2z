/*
 * Warmup 1: Build Adjacency List
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Given n nodes and edges, build a sorted adjacency list.
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> solve(int n, vector<vector<int>>& edges) {
    // TODO: Replace this with your solution
    return vector<vector<int>>(n);
}

int main() {
    int n, m; cin >> n >> m;
    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) cin >> edges[i][0] >> edges[i][1];
    auto adj = solve(n, edges);
    for (int i = 0; i < n; i++) {
        cout << i << ": [";
        for (int j = 0; j < (int)adj[i].size(); j++) {
            if (j > 0) cout << ", ";
            cout << adj[i][j];
        }
        cout << "]" << endl;
    }
    return 0;
}
