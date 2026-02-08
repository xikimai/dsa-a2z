/*
 * Practice 5: All Paths from Source to Target
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Find all paths from node 0 to node n-1 in a DAG.
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> solve(int n, vector<vector<int>>& edges) {
    // TODO: Replace this with your solution
    return {};
}

int main() {
    int n, m; cin >> n >> m;
    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) cin >> edges[i][0] >> edges[i][1];
    auto paths = solve(n, edges);
    for (auto& path : paths) {
        for (int i = 0; i < (int)path.size(); i++) {
            if (i > 0) cout << " -> ";
            cout << path[i];
        }
        cout << endl;
    }
    return 0;
}
