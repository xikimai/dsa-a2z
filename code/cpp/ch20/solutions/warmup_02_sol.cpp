#include <vector>
#include <queue>
#include <iostream>
using namespace std;

int solve(vector<vector<int>>& grid) {
    int rows = grid.size(), cols = grid[0].size();
    int count = 0;
    int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};

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
    int rows, cols;
    cin >> rows >> cols;
    vector<vector<int>> grid(rows, vector<int>(cols));
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            cin >> grid[i][j];
    cout << solve(grid) << endl;
    return 0;
}
