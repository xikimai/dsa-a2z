/*
 * Example 1: Grid BFS Basics
 * Chapter 20: Graphs II — Real Problems
 *
 * Demonstrates grid BFS, flood fill, and counting islands.
 */
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, -1, 1};

// Flood fill from (sr, sc) with new color
void floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
    int rows = image.size(), cols = image[0].size();
    int original = image[sr][sc];
    if (original == color) return;

    queue<pair<int,int>> q;
    q.push({sr, sc});
    image[sr][sc] = color;

    while (!q.empty()) {
        auto [r, c] = q.front(); q.pop();
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && image[nr][nc] == original) {
                image[nr][nc] = color;
                q.push({nr, nc});
            }
        }
    }
}

// Count islands (connected components of 1's)
int countIslands(vector<vector<int>> grid) {
    int rows = grid.size(), cols = grid[0].size();
    int count = 0;

    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++)
            if (grid[r][c] == 1) {
                count++;
                queue<pair<int,int>> q;
                q.push({r, c});
                grid[r][c] = 0;
                while (!q.empty()) {
                    auto [cr, cc] = q.front(); q.pop();
                    for (int d = 0; d < 4; d++) {
                        int nr = cr + dr[d], nc = cc + dc[d];
                        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                            grid[nr][nc] = 0;
                            q.push({nr, nc});
                        }
                    }
                }
            }
    return count;
}

int main() {
    cout << "=== Flood Fill Demo ===" << endl;
    vector<vector<int>> image = {{1,1,1},{1,1,0},{1,0,1}};
    floodFill(image, 1, 1, 2);
    for (auto& row : image) {
        for (int v : row) cout << v << " ";
        cout << endl;
    }

    cout << "\n=== Count Islands Demo ===" << endl;
    vector<vector<int>> grid = {{1,1,0,0,0},{1,1,0,0,0},{0,0,1,0,0},{0,0,0,1,1}};
    cout << "Islands: " << countIslands(grid) << endl;

    return 0;
}
