#include <vector>
#include <queue>
#include <iostream>
using namespace std;

int solve(vector<vector<int>>& grid) {
    int rows = grid.size(), cols = grid[0].size();
    int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};
    queue<pair<int,int>> q;

    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++)
            if ((r == 0 || r == rows-1 || c == 0 || c == cols-1) && grid[r][c] == 1) {
                q.push({r, c});
                grid[r][c] = 0;
            }

    while (!q.empty()) {
        auto [r, c] = q.front(); q.pop();
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                grid[nr][nc] = 0;
                q.push({nr, nc});
            }
        }
    }

    int count = 0;
    for (auto& row : grid)
        for (int v : row)
            if (v == 1) count++;
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
