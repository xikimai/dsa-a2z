/*
 * Solution for Warmup 3: Kruskal's MST
 * Chapter 29: Union-Find & Minimum Spanning Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

int solve(int n, vector<vector<int>>& edges) {
    if (n <= 1) return 0;
    vector<int> parent(n), rnk(n, 0);
    iota(parent.begin(), parent.end(), 0);
    function<int(int)> find = [&](int x) -> int {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };
    sort(edges.begin(), edges.end(), [](auto& a, auto& b) { return a[2] < b[2]; });
    int total = 0;
    for (auto& e : edges) {
        int rx = find(e[0]), ry = find(e[1]);
        if (rx != ry) {
            if (rnk[rx] < rnk[ry]) parent[rx] = ry;
            else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
            else { parent[ry] = rx; rnk[rx]++; }
            total += e[2];
        }
    }
    return total;
}

int main() { return 0; }
