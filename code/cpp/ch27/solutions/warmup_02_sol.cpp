/*
 * Solution for Warmup 2: Network Delay Time
 * Chapter 27: Shortest Paths — Finding the Best Route
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& times, int n, int k) {
    const int INF = 1e9;
    vector<vector<pair<int,int>>> adj(n + 1);
    for (auto& t : times) adj[t[0]].push_back({t[1], t[2]});
    vector<int> dist(n + 1, INF);
    dist[k] = 0;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0, k});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto [v, w] : adj[u])
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
    }
    int ans = *max_element(dist.begin() + 1, dist.end());
    return ans >= INF ? -1 : ans;
}

int main() { return 0; }
