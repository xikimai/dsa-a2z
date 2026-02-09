/*
 * Solution for Challenge 2: Making a Large Island
 * Chapter 29: Union-Find & Minimum Spanning Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& grid) {
    int n = grid.size();
    vector<int> parent(n * n), rnk(n * n, 0), sz(n * n, 1);
    for (int i = 0; i < n * n; i++) parent[i] = i;

    function<int(int)> find = [&](int x) -> int {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };
    auto unite = [&](int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return;
        if (rnk[rx] < rnk[ry]) { parent[rx] = ry; sz[ry] += sz[rx]; }
        else if (rnk[rx] > rnk[ry]) { parent[ry] = rx; sz[rx] += sz[ry]; }
        else { parent[ry] = rx; sz[rx] += sz[ry]; rnk[rx]++; }
    };

    int dirs2[][2] = {{0,1},{1,0}};
    for (int r = 0; r < n; r++)
        for (int c = 0; c < n; c++)
            if (grid[r][c] == 1)
                for (auto& d : dirs2) {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr < n && nc < n && grid[nr][nc] == 1)
                        unite(r * n + c, nr * n + nc);
                }

    int best = 0;
    for (int r = 0; r < n; r++)
        for (int c = 0; c < n; c++)
            if (grid[r][c] == 1)
                best = max(best, sz[find(r * n + c)]);

    int dirs4[][2] = {{-1,0},{1,0},{0,-1},{0,1}};
    for (int r = 0; r < n; r++)
        for (int c = 0; c < n; c++)
            if (grid[r][c] == 0) {
                set<int> seen;
                int total = 1;
                for (auto& d : dirs4) {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                        int root = find(nr * n + nc);
                        if (seen.insert(root).second) total += sz[root];
                    }
                }
                best = max(best, total);
            }
    return best;
}

int main() { return 0; }
