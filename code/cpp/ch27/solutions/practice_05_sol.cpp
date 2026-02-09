/*
 * Solution for Practice 5: Swim in Rising Water
 * Chapter 27: Shortest Paths — Finding the Best Route
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& grid) {
    int n = grid.size();
    const int INF = 1e9;
    vector<vector<int>> dist(n, vector<int>(n, INF));
    dist[0][0] = grid[0][0];
    priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, greater<>> pq;
    pq.push({grid[0][0], 0, 0});
    int dirs[][2] = {{0,1},{0,-1},{1,0},{-1,0}};
    while (!pq.empty()) {
        auto [d, r, c] = pq.top(); pq.pop();
        if (d > dist[r][c]) continue;
        if (r == n-1 && c == n-1) return d;
        for (auto& dir : dirs) {
            int nr = r+dir[0], nc = c+dir[1];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                int nd = max(d, grid[nr][nc]);
                if (nd < dist[nr][nc]) {
                    dist[nr][nc] = nd;
                    pq.push({nd, nr, nc});
                }
            }
        }
    }
    return dist[n-1][n-1];
}

int main() { return 0; }
