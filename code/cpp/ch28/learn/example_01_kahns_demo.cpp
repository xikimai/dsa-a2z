/*
 * Example 01: Kahn's Algorithm Demo — BFS Topological Sort
 * =========================================================
 * Chapter 28: Topological Sort — Ordering Dependencies
 *
 * Demonstrates Kahn's Algorithm step-by-step.
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<int> kahnsTopoSort(int n, vector<vector<int>>& edges) {
    vector<vector<int>> adj(n);
    vector<int> inDeg(n, 0);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        inDeg[e[1]]++;
    }
    queue<int> q;
    for (int i = 0; i < n; i++)
        if (inDeg[i] == 0) q.push(i);
    vector<int> result;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        result.push_back(u);
        for (int v : adj[u])
            if (--inDeg[v] == 0) q.push(v);
    }
    return result.size() == (size_t)n ? result : vector<int>{};
}

int main() {
    cout << "Kahn's Algorithm: BFS Topological Sort" << endl;
    cout << "=======================================" << endl;

    vector<vector<int>> edges = {{5,2},{5,0},{4,0},{4,1},{2,3},{3,1}};
    auto result = kahnsTopoSort(6, edges);
    cout << "DAG result: ";
    for (int x : result) cout << x << " ";
    cout << endl;

    vector<vector<int>> cycleEdges = {{0,1},{1,2},{2,0}};
    auto cycleResult = kahnsTopoSort(3, cycleEdges);
    cout << "Cycle result: ";
    if (cycleResult.empty()) cout << "(empty = cycle detected)";
    cout << endl;

    return 0;
}
