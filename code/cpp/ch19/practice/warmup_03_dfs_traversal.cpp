/*
 * Warmup 3: DFS Traversal
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Return DFS traversal order from source (smallest neighbor first).
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(int n, vector<vector<int>>& edges, int source) {
    // TODO: Replace this with your solution
    return {};
}

int main() {
    int n, m, source; cin >> n >> m >> source;
    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) cin >> edges[i][0] >> edges[i][1];
    auto result = solve(n, edges, source);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
