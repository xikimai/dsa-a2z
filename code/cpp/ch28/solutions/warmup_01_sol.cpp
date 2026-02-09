/*
 * Solution for Warmup 1: Topological Sort (Kahn's)
 * Chapter 28: Topological Sort — Ordering Dependencies
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
using namespace std;

vector<int> solve(int n, vector<vector<int>>& edges) {
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
    return (int)result.size() == n ? result : vector<int>{};
}

int main() { return 0; }
