/*
 * Solution for Warmup 3: Bellman-Ford SSSP
 * Chapter 27: Shortest Paths — Finding the Best Route
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(int n, vector<vector<int>>& edges, int src) {
    const int INF = 1e9;
    vector<int> dist(n, INF);
    dist[src] = 0;
    for (int i = 0; i < n - 1; i++)
        for (auto& e : edges)
            if (dist[e[0]] != INF && dist[e[0]] + e[2] < dist[e[1]])
                dist[e[1]] = dist[e[0]] + e[2];
    return dist;
}

int main() { return 0; }
