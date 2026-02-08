#include <vector>
#include <queue>
#include <iostream>
using namespace std;

int solve(vector<vector<int>>& grid) {
    int n = grid.size();
    int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};

    // Find first island via BFS
    queue<tuple<int,int,int>> mq; // multi-source BFS queue
    bool found = false;
    for (int r = 0; r < n && !found; r++)
        for (int c = 0; c < n && !found; c++)
            if (grid[r][c] == 1) {
                queue<pair<int,int>> bfs;
                bfs.push({r, c});
                grid[r][c] = 2;
                while (!bfs.empty()) {
                    auto [cr, cc] = bfs.front(); bfs.pop();
                    mq.push({cr, cc, 0});
                    for (int d = 0; d < 4; d++) {
                        int nr = cr + dr[d], nc = cc + dc[d];
                        if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                            grid[nr][nc] = 2;
                            bfs.push({nr, nc});
                        }
                    }
                }
                found = true;
            }

    // Multi-source BFS from island 1
    while (!mq.empty()) {
        auto [r, c, dist] = mq.front(); mq.pop();
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                if (grid[nr][nc] == 1) return dist;
                if (grid[nr][nc] == 0) {
                    grid[nr][nc] = 2;
                    mq.push({nr, nc, dist + 1});
                }
            }
        }
    }
    return -1;
}

int main() {
    int n;
    cin >> n;
    vector<vector<int>> grid(n, vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> grid[i][j];
    cout << solve(grid) << endl;
    return 0;
}
