/*
 * Solution for Practice 4: Min Cost to Connect All Points
 * Chapter 29: Union-Find & Minimum Spanning Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& points) {
    int n = points.size();
    if (n <= 1) return 0;
    vector<int> parent(n), rnk(n, 0);
    iota(parent.begin(), parent.end(), 0);
    function<int(int)> find = [&](int x) -> int {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };

    vector<tuple<int,int,int>> edges;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++) {
            int dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
            edges.push_back({dist, i, j});
        }
    sort(edges.begin(), edges.end());

    int total = 0, count = 0;
    for (auto [w, u, v] : edges) {
        int rx = find(u), ry = find(v);
        if (rx != ry) {
            if (rnk[rx] < rnk[ry]) parent[rx] = ry;
            else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
            else { parent[ry] = rx; rnk[rx]++; }
            total += w;
            if (++count == n - 1) break;
        }
    }
    return total;
}

int main() { return 0; }
