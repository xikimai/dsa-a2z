/*
 * Example 02: Bellman-Ford Algorithm — Handling Negative Weights
 * Chapter 27: Shortest Paths — Finding the Best Route
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

vector<int> bellmanFord(int n, vector<vector<int>>& edges, int src) {
    const int INF = 1e9;
    vector<int> dist(n, INF);
    dist[src] = 0;

    for (int round = 1; round < n; round++) {
        bool updated = false;
        for (auto& e : edges) {
            if (dist[e[0]] != INF && dist[e[0]] + e[2] < dist[e[1]]) {
                cout << "  Round " << round << ": Relax " << e[0] << " -> " << e[1]
                     << ": " << dist[e[1]] << " -> " << dist[e[0]] + e[2] << "\n";
                dist[e[1]] = dist[e[0]] + e[2];
                updated = true;
            }
        }
        if (!updated) {
            cout << "  Round " << round << ": No updates — early stop!\n";
            break;
        }
    }

    for (auto& e : edges) {
        if (dist[e[0]] != INF && dist[e[0]] + e[2] < dist[e[1]]) {
            cout << "  NEGATIVE CYCLE DETECTED!\n";
            return {};
        }
    }
    return dist;
}

int main() {
    vector<vector<int>> edges = {{0,1,-1},{0,2,4},{1,2,3},{1,3,2},{1,4,2},{3,2,5},{3,1,1},{4,3,-3}};
    cout << "Bellman-Ford Algorithm Demo\n";
    cout << "==========================\n";
    auto dist = bellmanFord(5, edges, 0);
    if (!dist.empty()) {
        cout << "Distances:";
        for (int d : dist) cout << " " << d;
        cout << "\n";
    }
    return 0;
}
