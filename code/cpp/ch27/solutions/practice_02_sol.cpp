/*
 * Solution for Practice 2: Path with Minimum Effort
 * Chapter 27: Shortest Paths — Finding the Best Route
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& heights) {
    int m = heights.size(), n = heights[0].size();
    const int INF = 1e9;
    vector<vector<int>> dist(m, vector<int>(n, INF));
    dist[0][0] = 0;
    priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, greater<>> pq;
    pq.push({0, 0, 0});
    int dirs[][2] = {{0,1},{0,-1},{1,0},{-1,0}};
    while (!pq.empty()) {
        auto [effort, r, c] = pq.top(); pq.pop();
        if (effort > dist[r][c]) continue;
        if (r == m-1 && c == n-1) return effort;
        for (auto& d : dirs) {
            int nr = r+d[0], nc = c+d[1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                int ne = max(effort, abs(heights[r][c] - heights[nr][nc]));
                if (ne < dist[nr][nc]) {
                    dist[nr][nc] = ne;
                    pq.push({ne, nr, nc});
                }
            }
        }
    }
    return dist[m-1][n-1];
}

int main() { return 0; }
