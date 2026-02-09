/*
 * Example 01: Dijkstra's Algorithm — Step-by-Step Demo
 * Chapter 27: Shortest Paths — Finding the Best Route
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<int> dijkstra(int n, vector<vector<int>>& edges, int src) {
    const int INF = 1e9;
    vector<vector<pair<int,int>>> adj(n);
    for (auto& e : edges)
        adj[e[0]].push_back({e[1], e[2]});

    vector<int> dist(n, INF);
    dist[src] = 0;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0, src});

    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        cout << "  Process node " << u << " (distance = " << d << ")\n";
        for (auto [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                cout << "    Relax " << u << " -> " << v
                     << ": " << dist[v] << " -> " << dist[u] + w << "\n";
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}

int main() {
    vector<vector<int>> edges = {{0,1,4},{0,2,1},{2,1,2},{1,3,5},{2,3,8},{3,4,1}};
    cout << "Dijkstra's Algorithm Demo\n";
    cout << "=========================\n";
    auto dist = dijkstra(5, edges, 0);
    cout << "Distances:";
    for (int d : dist) cout << " " << d;
    cout << "\n";
    return 0;
}
