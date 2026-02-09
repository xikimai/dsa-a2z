/*
 * Solution for Challenge 3: Binary Tree Cameras
 * Chapter 31: Advanced DP — Bitmask, Interval, Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

const int INF = 1000000;

int solve(int n, vector<vector<int>>& edges) {
    if (n == 0) return 0;
    if (n <= 2) return 1;

    vector<vector<int>> adj(n);
    for (auto& e : edges) { adj[e[0]].push_back(e[1]); adj[e[1]].push_back(e[0]); }

    // dp[u][0]=not covered, dp[u][1]=covered no camera, dp[u][2]=has camera
    vector<array<int,3>> dp(n, {0, 0, 0});
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
        vector<int> children;
        for (int v : adj[u]) if (v != par[u]) children.push_back(v);

        if (children.empty()) {
            dp[u] = {0, INF, 1};
            continue;
        }

        int cam = 1;
        for (int v : children) cam += min({dp[v][0], dp[v][1], dp[v][2]});

        int notCov = 0;
        for (int v : children) notCov += min(dp[v][1], dp[v][2]);

        int base = 0;
        for (int v : children) base += min(dp[v][1], dp[v][2]);

        int cov = INF;
        bool allPrefer1 = true;
        for (int v : children)
            if (dp[v][2] <= dp[v][1]) { allPrefer1 = false; break; }

        if (!allPrefer1) {
            cov = base;
        } else {
            int minUp = INF;
            for (int v : children) minUp = min(minUp, dp[v][2] - dp[v][1]);
            cov = base + minUp;
        }

        dp[u] = {notCov, cov, cam};
    }

    return min(dp[0][1], dp[0][2]);
}

int main() { return 0; }
