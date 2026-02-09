/*
 * Solution for Warmup 3: House Robber on Tree
 * Chapter 31: Advanced DP — Bitmask, Interval, Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int solve(int n, vector<int>& values, vector<vector<int>>& edges) {
    if (n == 0) return 0;
    if (n == 1) return values[0];

    vector<vector<int>> adj(n);
    for (auto& e : edges) { adj[e[0]].push_back(e[1]); adj[e[1]].push_back(e[0]); }

    vector<array<int,2>> dp(n, {0, 0});
    vector<bool> visited(n, false);
    vector<int> par(n, -1), order;

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

    for (int idx = order.size() - 1; idx >= 0; idx--) {
        int u = order[idx];
        dp[u][1] = values[u];
        for (int v : adj[u]) {
            if (v == par[u]) continue;
            dp[u][0] += max(dp[v][0], dp[v][1]);
            dp[u][1] += dp[v][0];
        }
    }

    return max(dp[0][0], dp[0][1]);
}

int main() { return 0; }
