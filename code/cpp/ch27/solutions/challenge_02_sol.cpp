/*
 * Solution for Challenge 2: Shortest Path with Alternating Colors
 * Chapter 27: Shortest Paths — Finding the Best Route
 */
#include <algorithm>
#include <climits>
#include <deque>
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(int n, vector<vector<int>>& redEdges, vector<vector<int>>& blueEdges) {
    const int INF = 1e9;
    // adj[node][color] where 0=red, 1=blue
    vector<vector<vector<int>>> adj(n, vector<vector<int>>(2));
    for (auto& e : redEdges) adj[e[0]][0].push_back(e[1]);
    for (auto& e : blueEdges) adj[e[0]][1].push_back(e[1]);

    vector<vector<int>> dist(n, vector<int>(2, INF));
    dist[0][0] = 0;
    dist[0][1] = 0;
    deque<pair<int,int>> q;
    q.push_back({0, 0});
    q.push_back({0, 1});

    while (!q.empty()) {
        auto [u, color] = q.front(); q.pop_front();
        int nextColor = 1 - color;
        for (int v : adj[u][nextColor]) {
            if (dist[u][color] + 1 < dist[v][nextColor]) {
                dist[v][nextColor] = dist[u][color] + 1;
                q.push_back({v, nextColor});
            }
        }
    }

    vector<int> result(n);
    for (int i = 0; i < n; i++) {
        int best = min(dist[i][0], dist[i][1]);
        result[i] = best >= INF ? -1 : best;
    }
    return result;
}

int main() { return 0; }
