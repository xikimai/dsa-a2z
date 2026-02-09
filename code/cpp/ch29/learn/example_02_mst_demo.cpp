/*
 * Example 02: MST Demo — Kruskal's and Prim's Side by Side
 * ==========================================================
 * Chapter 29: Union-Find & Minimum Spanning Trees
 *
 * Demonstrates both MST algorithms on the same graph.
 */

#include <algorithm>
#include <climits>
#include <functional>
#include <iostream>
#include <numeric>
#include <queue>
#include <vector>
using namespace std;

int kruskalMST(int n, vector<vector<int>> edges) {
    vector<int> parent(n), rnk(n, 0);
    iota(parent.begin(), parent.end(), 0);
    function<int(int)> find = [&](int x) -> int {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };

    sort(edges.begin(), edges.end(), [](auto& a, auto& b) { return a[2] < b[2]; });
    int total = 0;
    for (auto& e : edges) {
        int rx = find(e[0]), ry = find(e[1]);
        if (rx != ry) {
            if (rnk[rx] < rnk[ry]) parent[rx] = ry;
            else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
            else { parent[ry] = rx; rnk[rx]++; }
            total += e[2];
        }
    }
    return total;
}

int primMST(int n, vector<vector<int>>& edges) {
    vector<vector<pair<int,int>>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back({e[2], e[1]});
        adj[e[1]].push_back({e[2], e[0]});
    }
    vector<bool> vis(n, false);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0, 0});
    int total = 0, count = 0;
    while (!pq.empty() && count < n) {
        auto [w, u] = pq.top(); pq.pop();
        if (vis[u]) continue;
        vis[u] = true;
        total += w;
        count++;
        for (auto [nw, nv] : adj[u])
            if (!vis[nv]) pq.push({nw, nv});
    }
    return total;
}

int main() {
    int n = 5;
    vector<vector<int>> edges = {
        {0,1,4}, {0,2,8}, {1,2,2}, {1,3,6}, {2,3,3}, {2,4,9}, {3,4,5}
    };
    cout << "MST Demo" << endl;
    cout << "  Kruskal's: " << kruskalMST(n, edges) << endl;
    cout << "  Prim's:    " << primMST(n, edges) << endl;
    return 0;
}
