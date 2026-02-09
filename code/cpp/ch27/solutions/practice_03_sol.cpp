/*
 * Solution for Practice 3: Find City with Smallest Neighbors at Threshold
 * Chapter 27: Shortest Paths — Finding the Best Route
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

int solve(int n, vector<vector<int>>& edges, int threshold) {
    const int INF = 1e9;
    vector<vector<int>> dist(n, vector<int>(n, INF));
    for (int i = 0; i < n; i++) dist[i][i] = 0;
    for (auto& e : edges) {
        dist[e[0]][e[1]] = min(dist[e[0]][e[1]], e[2]);
        dist[e[1]][e[0]] = min(dist[e[1]][e[0]], e[2]);
    }
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
    int bestCity = -1, bestCount = n + 1;
    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = 0; j < n; j++)
            if (j != i && dist[i][j] <= threshold) count++;
        if (count <= bestCount) {
            bestCount = count;
            bestCity = i;
        }
    }
    return bestCity;
}

int main() { return 0; }
