/*
 * Example 2: Multi-Source BFS
 * Chapter 20: Graphs II — Real Problems
 *
 * Demonstrates rotten oranges via multi-source BFS.
 */
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, -1, 1};

int rottenOranges(vector<vector<int>>& grid) {
    int rows = grid.size(), cols = grid[0].size();
    queue<pair<int,int>> q;
    int fresh = 0;

    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++) {
            if (grid[r][c] == 2) q.push({r, c});
            else if (grid[r][c] == 1) fresh++;
        }

    if (fresh == 0) return 0;

    int minutes = 0;
    while (!q.empty() && fresh > 0) {
        minutes++;
        int sz = q.size();
        for (int i = 0; i < sz; i++) {
            auto [r, c] = q.front(); q.pop();
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d], nc = c + dc[d];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                    grid[nr][nc] = 2;
                    fresh--;
                    q.push({nr, nc});
                }
            }
        }
    }
    return fresh == 0 ? minutes : -1;
}

int main() {
    vector<vector<int>> grid = {{2,1,1},{1,1,0},{0,1,1}};
    cout << "Rotten oranges minutes: " << rottenOranges(grid) << endl; // Expected: 4
    return 0;
}
