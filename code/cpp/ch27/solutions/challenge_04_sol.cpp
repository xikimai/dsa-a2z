/*
 * Solution for Challenge 4: Path with Maximum Minimum Value
 * Chapter 27: Shortest Paths — Finding the Best Route
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    vector<vector<int>> dist(m, vector<int>(n, -1));
    dist[0][0] = grid[0][0];
    // Max-heap
    priority_queue<tuple<int,int,int>> pq;
    pq.push({grid[0][0], 0, 0});
    int dirs[][2] = {{0,1},{0,-1},{1,0},{-1,0}};
    while (!pq.empty()) {
        auto [d, r, c] = pq.top(); pq.pop();
        if (d < dist[r][c]) continue;
        if (r == m-1 && c == n-1) return d;
        for (auto& dir : dirs) {
            int nr = r+dir[0], nc = c+dir[1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                int nv = min(d, grid[nr][nc]);
                if (nv > dist[nr][nc]) {
                    dist[nr][nc] = nv;
                    pq.push({nv, nr, nc});
                }
            }
        }
    }
    return dist[m-1][n-1];
}

int main() { return 0; }
