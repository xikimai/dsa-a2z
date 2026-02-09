/*
 * Solution for Practice 1: Cheapest Flights Within K Stops
 * Chapter 27: Shortest Paths — Finding the Best Route
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

int solve(int n, vector<vector<int>>& flights, int src, int dst, int k) {
    const int INF = 1e9;
    vector<int> dist(n, INF);
    dist[src] = 0;
    for (int i = 0; i <= k; i++) {
        vector<int> prev = dist;
        for (auto& f : flights)
            if (prev[f[0]] != INF && prev[f[0]] + f[2] < dist[f[1]])
                dist[f[1]] = prev[f[0]] + f[2];
    }
    return dist[dst] >= INF ? -1 : dist[dst];
}

int main() { return 0; }
