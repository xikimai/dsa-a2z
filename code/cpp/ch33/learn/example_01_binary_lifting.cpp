/*
 * Example 01: Binary Lifting — LCA in O(log n)
 * ==============================================
 * Chapter 33: Advanced Trees & Graph Algorithms
 *
 * Demonstrates binary lifting for fast LCA queries.
 */

#include <algorithm>
#include <climits>
#include <cmath>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

class BinaryLifting {
public:
    vector<vector<int>> up;
    vector<int> depth;
    int LOG;

    BinaryLifting(int n, vector<pair<int,int>>& edges, int root = 0) {
        vector<vector<int>> adj(n);
        for (auto [u, v] : edges) {
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        LOG = max(1, (int)ceil(log2(n)) + 1);
        up.assign(n, vector<int>(LOG, -1));
        depth.assign(n, 0);

        vector<bool> visited(n, false);
        queue<int> q;
        q.push(root);
        visited[root] = true;
        while (!q.empty()) {
            int node = q.front(); q.pop();
            for (int nb : adj[node]) {
                if (!visited[nb]) {
                    visited[nb] = true;
                    depth[nb] = depth[node] + 1;
                    up[nb][0] = node;
                    q.push(nb);
                }
            }
        }

        for (int k = 1; k < LOG; k++)
            for (int v = 0; v < n; v++)
                if (up[v][k - 1] != -1)
                    up[v][k] = up[up[v][k - 1]][k - 1];
    }

    int lca(int u, int v) {
        if (depth[u] < depth[v]) swap(u, v);
        int diff = depth[u] - depth[v];
        for (int k = 0; k < LOG; k++)
            if ((diff >> k) & 1) u = up[u][k];
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; k--)
            if (up[u][k] != up[v][k]) { u = up[u][k]; v = up[v][k]; }
        return up[u][0];
    }
};

int main() {
    cout << "Binary Lifting: LCA Demo" << endl;

    vector<pair<int,int>> edges = {{0,1},{0,2},{1,3},{1,4},{2,5},{5,6}};
    BinaryLifting bl(7, edges);

    cout << "  LCA(3,4) = " << bl.lca(3, 4) << endl; // 1
    cout << "  LCA(3,6) = " << bl.lca(3, 6) << endl; // 0
    cout << "  LCA(4,5) = " << bl.lca(4, 5) << endl; // 0

    return 0;
}
