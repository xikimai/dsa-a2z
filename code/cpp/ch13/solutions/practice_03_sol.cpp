/*
 * Solution for Practice 3: Rat in a Maze
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * APPROACH: Backtrack from (0,0), try D/L/R/U in alphabetical order.
 * TIME:  O(4^(n^2))
 * SPACE: O(n^2)
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> solve(vector<vector<int>> maze) {
    int n = maze.size();
    if (n == 0 || maze[0][0] == 0) return {};

    vector<string> result;
    vector<vector<bool>> visited(n, vector<bool>(n, false));
    // D, L, R, U — alphabetical order
    int dr[] = {1, 0, 0, -1};
    int dc[] = {0, -1, 1, 0};
    char dir[] = {'D', 'L', 'R', 'U'};

    function<void(int, int, string)> backtrack = [&](int r, int c, string path) {
        if (r == n - 1 && c == n - 1) {
            result.push_back(path);
            return;
        }
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n &&
                maze[nr][nc] == 1 && !visited[nr][nc]) {
                visited[nr][nc] = true;
                backtrack(nr, nc, path + dir[d]);
                visited[nr][nc] = false;
            }
        }
    };

    visited[0][0] = true;
    backtrack(0, 0, "");
    return result;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<vector<int>> maze(n, vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> maze[i][j];
    vector<string> result = solve(maze);
    for (auto& path : result) cout << path << endl;
    return 0;
}
