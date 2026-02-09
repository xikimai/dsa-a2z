/*
 * Example 02: DFS-Based Topological Sort with Cycle Detection
 * =============================================================
 * Chapter 28: Topological Sort — Ordering Dependencies
 *
 * Demonstrates DFS topo sort with three-color cycle detection.
 */

#include <algorithm>
#include <climits>
#include <functional>
#include <iostream>
#include <vector>
using namespace std;

vector<int> dfsTopoSort(int n, vector<vector<int>>& edges) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) adj[e[0]].push_back(e[1]);

    vector<int> color(n, 0); // 0=white, 1=gray, 2=black
    vector<int> stk;
    bool hasCycle = false;

    function<void(int)> dfs = [&](int u) {
        if (hasCycle) return;
        color[u] = 1;
        for (int v : adj[u]) {
            if (color[v] == 1) { hasCycle = true; return; }
            if (color[v] == 0) dfs(v);
        }
        color[u] = 2;
        stk.push_back(u);
    };

    for (int i = 0; i < n; i++)
        if (color[i] == 0) dfs(i);

    if (hasCycle) return {};
    reverse(stk.begin(), stk.end());
    return stk;
}

int main() {
    cout << "DFS Topological Sort: Three-Color Cycle Detection" << endl;
    cout << "==================================================" << endl;

    vector<vector<int>> edges = {{5,2},{5,0},{4,0},{4,1},{2,3},{3,1}};
    auto result = dfsTopoSort(6, edges);
    cout << "DAG result: ";
    for (int x : result) cout << x << " ";
    cout << endl;

    vector<vector<int>> cycleEdges = {{0,1},{1,2},{2,0}};
    auto cycleResult = dfsTopoSort(3, cycleEdges);
    cout << "Cycle result: ";
    if (cycleResult.empty()) cout << "(empty = cycle detected)";
    cout << endl;

    return 0;
}
