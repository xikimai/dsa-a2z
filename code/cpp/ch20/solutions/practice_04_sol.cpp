#include <vector>
#include <queue>
#include <iostream>
using namespace std;

int solve(vector<vector<int>>& grid) {
    int n = grid.size();
    if (grid[0][0] == 1 || grid[n-1][n-1] == 1) return -1;
    if (n == 1) return 1;

    int dirs[][2] = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
    queue<tuple<int,int,int>> q;
    q.push({0, 0, 1});
    grid[0][0] = 1;

    while (!q.empty()) {
        auto [r, c, dist] = q.front(); q.pop();
        for (auto& d : dirs) {
            int nr = r + d[0], nc = c + d[1];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                if (nr == n-1 && nc == n-1) return dist + 1;
                grid[nr][nc] = 1;
                q.push({nr, nc, dist + 1});
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
