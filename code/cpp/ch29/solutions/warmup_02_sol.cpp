/*
 * Solution for Warmup 2: Redundant Connection (1-indexed)
 * Chapter 29: Union-Find & Minimum Spanning Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

vector<int> solve(vector<vector<int>>& edges) {
    int n = edges.size();
    vector<int> parent(n + 1), rnk(n + 1, 0);
    iota(parent.begin(), parent.end(), 0);
    function<int(int)> find = [&](int x) -> int {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };
    for (auto& e : edges) {
        int rx = find(e[0]), ry = find(e[1]);
        if (rx == ry) return e;
        if (rnk[rx] < rnk[ry]) parent[rx] = ry;
        else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
        else { parent[ry] = rx; rnk[rx]++; }
    }
    return {};
}

int main() { return 0; }
