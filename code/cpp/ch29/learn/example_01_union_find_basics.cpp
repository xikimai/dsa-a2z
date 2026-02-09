/*
 * Example 01: Union-Find Basics — Step-by-Step DSU
 * ==================================================
 * Chapter 29: Union-Find & Minimum Spanning Trees
 *
 * Demonstrates Union-Find with path compression and union by rank.
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

class UnionFind {
public:
    vector<int> parent, rnk;

    UnionFind(int n) : parent(n), rnk(n, 0) {
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]); // path compression
        return parent[x];
    }

    bool unite(int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return false;
        if (rnk[rx] < rnk[ry]) parent[rx] = ry;
        else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
        else { parent[ry] = rx; rnk[rx]++; }
        return true;
    }
};

int main() {
    cout << "Union-Find Basics" << endl;

    // 5 nodes, connect some
    UnionFind uf(5);
    uf.unite(0, 1);
    uf.unite(1, 2);
    uf.unite(3, 4);

    cout << "  find(0)=" << uf.find(0) << ", find(2)=" << uf.find(2)
         << ", same? " << (uf.find(0) == uf.find(2) ? "true" : "false") << endl;
    cout << "  find(0)=" << uf.find(0) << ", find(3)=" << uf.find(3)
         << ", same? " << (uf.find(0) == uf.find(3) ? "true" : "false") << endl;

    // Count components
    UnionFind uf2(5);
    int components = 5;
    vector<pair<int,int>> edges = {{0,1},{1,2},{3,4}};
    for (auto [u, v] : edges)
        if (uf2.unite(u, v)) components--;
    cout << "  Components: " << components << endl; // 2

    return 0;
}
