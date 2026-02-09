/*
 * Solution for Practice 1: Unique Paths III
 * Chapter 24: Dynamic Programming II — Grids and Paths
 */

#include <algorithm>
#include <climits>
#include <functional>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    int startR = 0, startC = 0, empty = 0;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) { startR = i; startC = j; empty++; }
            else if (grid[i][j] == 0) empty++;
        }
    int result = 0;
    int dx[] = {0,0,1,-1}, dy[] = {1,-1,0,0};
    function<void(int,int,int)> dfs = [&](int r, int c, int rem) {
        if (grid[r][c] == 2) { if (rem == 0) result++; return; }
        int tmp = grid[r][c];
        grid[r][c] = -2;
        for (int d = 0; d < 4; d++) {
            int nr = r+dx[d], nc = c+dy[d];
            if (nr>=0 && nr<m && nc>=0 && nc<n && grid[nr][nc]!=-1 && grid[nr][nc]!=-2)
                dfs(nr, nc, rem-1);
        }
        grid[r][c] = tmp;
    };
    dfs(startR, startC, empty);
    return result;
}

int main() { return 0; }
