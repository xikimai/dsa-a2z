/*
 * Solution for Warmup 4: Shortest Path in Binary Matrix
 * Chapter 27: Shortest Paths — Finding the Best Route
 */
#include <algorithm>
#include <climits>
#include <deque>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& grid) {
    int n = grid.size();
    if (grid[0][0] == 1 || grid[n-1][n-1] == 1) return -1;
    if (n == 1) return 1;
    int dirs[][2] = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
    deque<tuple<int,int,int>> q;
    q.push_back({0, 0, 1});
    grid[0][0] = 1;
    while (!q.empty()) {
        auto [r, c, len] = q.front(); q.pop_front();
        for (auto& d : dirs) {
            int nr = r+d[0], nc = c+d[1];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                if (nr == n-1 && nc == n-1) return len + 1;
                grid[nr][nc] = 1;
                q.push_back({nr, nc, len + 1});
            }
        }
    }
    return -1;
}

int main() { return 0; }
