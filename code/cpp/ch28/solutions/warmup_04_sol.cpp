/*
 * Solution for Warmup 4: Detect Cycle in Directed Graph
 * Chapter 28: Topological Sort — Ordering Dependencies
 */
#include <algorithm>
#include <climits>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool solve(int n, vector<vector<int>>& edges) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) adj[e[0]].push_back(e[1]);
    vector<int> color(n, 0);

    function<bool(int)> hasCycle = [&](int u) -> bool {
        color[u] = 1;
        for (int v : adj[u]) {
            if (color[v] == 1) return true;
            if (color[v] == 0 && hasCycle(v)) return true;
        }
        color[u] = 2;
        return false;
    };

    for (int i = 0; i < n; i++)
        if (color[i] == 0 && hasCycle(i)) return false;
    return true;
}

int main() { return 0; }
