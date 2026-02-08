#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <iostream>
using namespace std;

int solve(vector<vector<int>>& grid) {
    int n = grid.size();
    vector<vector<int>> islandId(n, vector<int>(n, 0));
    unordered_map<int, int> islandSize;
    int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};
    int currentId = 2;

    for (int r = 0; r < n; r++)
        for (int c = 0; c < n; c++)
            if (grid[r][c] == 1 && islandId[r][c] == 0) {
                queue<pair<int,int>> q;
                q.push({r, c});
                islandId[r][c] = currentId;
                int sz = 0;
                while (!q.empty()) {
                    auto [cr, cc] = q.front(); q.pop();
                    sz++;
                    for (int d = 0; d < 4; d++) {
                        int nr = cr + dr[d], nc = cc + dc[d];
                        if (nr >= 0 && nr < n && nc >= 0 && nc < n
                            && grid[nr][nc] == 1 && islandId[nr][nc] == 0) {
                            islandId[nr][nc] = currentId;
                            q.push({nr, nc});
                        }
                    }
                }
                islandSize[currentId] = sz;
                currentId++;
            }

    if (islandSize.empty()) return 1;

    int maxSize = 0;
    for (auto& [id, sz] : islandSize) maxSize = max(maxSize, sz);

    for (int r = 0; r < n; r++)
        for (int c = 0; c < n; c++)
            if (grid[r][c] == 0) {
                unordered_set<int> neighborIds;
                for (int d = 0; d < 4; d++) {
                    int nr = r + dr[d], nc = c + dc[d];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && islandId[nr][nc] != 0)
                        neighborIds.insert(islandId[nr][nc]);
                }
                int total = 1;
                for (int id : neighborIds) total += islandSize[id];
                maxSize = max(maxSize, total);
            }
    return maxSize;
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
