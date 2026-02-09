/*
 * Solution for Challenge 1: Minimum Obstacle Removal — 0-1 BFS
 * Chapter 27: Shortest Paths — Finding the Best Route
 */
#include <algorithm>
#include <climits>
#include <deque>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    const int INF = 1e9;
    vector<vector<int>> dist(m, vector<int>(n, INF));
    dist[0][0] = 0;
    deque<pair<int,int>> dq;
    dq.push_front({0, 0});
    int dirs[][2] = {{0,1},{0,-1},{1,0},{-1,0}};
    while (!dq.empty()) {
        auto [r, c] = dq.front(); dq.pop_front();
        for (auto& d : dirs) {
            int nr = r+d[0], nc = c+d[1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                int cost = grid[nr][nc];
                if (dist[r][c] + cost < dist[nr][nc]) {
                    dist[nr][nc] = dist[r][c] + cost;
                    if (cost == 0) dq.push_front({nr, nc});
                    else dq.push_back({nr, nc});
                }
            }
        }
    }
    return dist[m-1][n-1];
}

int main() { return 0; }
