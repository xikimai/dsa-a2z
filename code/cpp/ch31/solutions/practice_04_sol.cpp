/*
 * Solution for Practice 4: Tree Diameter via DP
 * Chapter 31: Advanced DP — Bitmask, Interval, Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int solve(int n, vector<vector<int>>& edges) {
    if (n <= 1) return 0;

    vector<vector<int>> adj(n);
    for (auto& e : edges) { adj[e[0]].push_back(e[1]); adj[e[1]].push_back(e[0]); }

    vector<int> depth(n, 0), par(n, -1);
    vector<bool> visited(n, false);
    vector<int> order;

    stack<int> stk;
    stk.push(0);
    while (!stk.empty()) {
        int u = stk.top(); stk.pop();
        if (visited[u]) continue;
        visited[u] = true;
        order.push_back(u);
        for (int v : adj[u])
            if (!visited[v]) { par[v] = u; stk.push(v); }
    }

    int diameter = 0;
    for (int idx = order.size() - 1; idx >= 0; idx--) {
        int u = order[idx];
        int top1 = 0, top2 = 0;
        for (int v : adj[u]) {
            if (v == par[u]) continue;
            int d = depth[v] + 1;
            if (d >= top1) { top2 = top1; top1 = d; }
            else if (d > top2) top2 = d;
        }
        depth[u] = top1;
        diameter = max(diameter, top1 + top2);
    }

    return diameter;
}

int main() { return 0; }
