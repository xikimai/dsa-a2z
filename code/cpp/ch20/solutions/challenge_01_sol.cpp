#include <vector>
#include <queue>
#include <climits>
#include <iostream>
using namespace std;

void solve(vector<vector<int>>& rooms) {
    int rows = rooms.size(), cols = rooms[0].size();
    int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};
    queue<pair<int,int>> q;
    int INF = 2147483647;

    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++)
            if (rooms[r][c] == 0)
                q.push({r, c});

    while (!q.empty()) {
        auto [r, c] = q.front(); q.pop();
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && rooms[nr][nc] == INF) {
                rooms[nr][nc] = rooms[r][c] + 1;
                q.push({nr, nc});
            }
        }
    }
}

int main() {
    int rows, cols;
    cin >> rows >> cols;
    vector<vector<int>> rooms(rows, vector<int>(cols));
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            cin >> rooms[i][j];
    solve(rooms);
    for (auto& row : rooms) {
        for (int v : row) cout << v << " ";
        cout << "\n";
    }
    return 0;
}
