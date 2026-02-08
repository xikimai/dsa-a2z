#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;

bool canReach(vector<vector<int>>& grid, int n, int t) {
    if (grid[0][0] > t) return false;
    int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};
    vector<vector<bool>> visited(n, vector<bool>(n, false));
    queue<pair<int,int>> q;
    q.push({0, 0});
    visited[0][0] = true;
    while (!q.empty()) {
        auto [r, c] = q.front(); q.pop();
        if (r == n-1 && c == n-1) return true;
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n
                && !visited[nr][nc] && grid[nr][nc] <= t) {
                visited[nr][nc] = true;
                q.push({nr, nc});
            }
        }
    }
    return false;
}

int solve(vector<vector<int>>& grid) {
    int n = grid.size();
    int lo = max(grid[0][0], grid[n-1][n-1]);
    int hi = n * n - 1;

    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (canReach(grid, n, mid))
            hi = mid;
        else
            lo = mid + 1;
    }
    return lo;
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
