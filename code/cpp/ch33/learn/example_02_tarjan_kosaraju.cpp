/*
 * Example 02: Tarjan's Bridges & Kosaraju's SCC
 * ===============================================
 * Chapter 33: Advanced Trees & Graph Algorithms
 *
 * Demonstrates bridge finding and SCC detection.
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

// ── Tarjan's Bridges ─────────────────────────────────────

int timer_val = 0;

void dfs_bridge(int u, int parent, vector<vector<int>>& adj, vector<int>& disc,
                vector<int>& low, vector<pair<int,int>>& bridges) {
    disc[u] = low[u] = timer_val++;
    for (int v : adj[u]) {
        if (disc[v] == -1) {
            dfs_bridge(v, u, adj, disc, low, bridges);
            low[u] = min(low[u], low[v]);
            if (low[v] > disc[u])
                bridges.push_back({min(u,v), max(u,v)});
        } else if (v != parent) {
            low[u] = min(low[u], disc[v]);
        }
    }
}

// ── Kosaraju's SCC ───────────────────────────────────────

void dfs1(int u, vector<vector<int>>& adj, vector<bool>& vis, vector<int>& order) {
    vis[u] = true;
    for (int v : adj[u]) if (!vis[v]) dfs1(v, adj, vis, order);
    order.push_back(u);
}

void dfs2(int u, int label, vector<vector<int>>& radj, vector<int>& comp) {
    comp[u] = label;
    for (int v : radj[u]) if (comp[v] == -1) dfs2(v, label, radj, comp);
}

int main() {
    cout << "Tarjan's Bridges:" << endl;
    int n = 5;
    vector<vector<int>> adj(n);
    vector<pair<int,int>> edges = {{0,1},{1,2},{2,0},{1,3},{3,4}};
    for (auto [u, v] : edges) { adj[u].push_back(v); adj[v].push_back(u); }

    vector<int> disc(n, -1), low(n, 0);
    vector<pair<int,int>> bridges;
    timer_val = 0;
    for (int i = 0; i < n; i++)
        if (disc[i] == -1) dfs_bridge(i, -1, adj, disc, low, bridges);
    for (auto [u, v] : bridges)
        cout << "  Bridge: " << u << "-" << v << endl;

    cout << "\nKosaraju's SCC:" << endl;
    vector<vector<int>> dadj(n), radj(n);
    vector<pair<int,int>> dedges = {{0,1},{1,2},{2,0},{1,3},{3,4}};
    for (auto [u, v] : dedges) { dadj[u].push_back(v); radj[v].push_back(u); }

    vector<bool> vis(n, false);
    vector<int> order;
    for (int i = 0; i < n; i++) if (!vis[i]) dfs1(i, dadj, vis, order);

    vector<int> comp(n, -1);
    int count = 0;
    for (int i = n - 1; i >= 0; i--)
        if (comp[order[i]] == -1) dfs2(order[i], count++, radj, comp);
    cout << "  Number of SCCs: " << count << endl; // 3

    return 0;
}
