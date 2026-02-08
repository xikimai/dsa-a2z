#include <vector>
#include <queue>
#include <climits>
#include <iostream>
using namespace std;

vector<vector<int>> solve(vector<vector<int>>& mat) {
    int rows = mat.size(), cols = mat[0].size();
    vector<vector<int>> dist(rows, vector<int>(cols, INT_MAX));
    queue<pair<int,int>> q;
    int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};

    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++)
            if (mat[r][c] == 0) {
                dist[r][c] = 0;
                q.push({r, c});
            }

    while (!q.empty()) {
        auto [r, c] = q.front(); q.pop();
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && dist[nr][nc] > dist[r][c] + 1) {
                dist[nr][nc] = dist[r][c] + 1;
                q.push({nr, nc});
            }
        }
    }
    return dist;
}

int main() {
    int rows, cols;
    cin >> rows >> cols;
    vector<vector<int>> mat(rows, vector<int>(cols));
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            cin >> mat[i][j];
    auto result = solve(mat);
    for (auto& row : result) {
        for (int v : row) cout << v << " ";
        cout << "\n";
    }
    return 0;
}
