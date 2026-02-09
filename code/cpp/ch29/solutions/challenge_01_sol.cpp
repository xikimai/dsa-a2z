/*
 * Solution for Challenge 1: Operations to Make Network Connected
 * Chapter 29: Union-Find & Minimum Spanning Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

int solve(int n, vector<vector<int>>& connections) {
    if ((int)connections.size() < n - 1) return -1;
    vector<int> parent(n), rnk(n, 0);
    iota(parent.begin(), parent.end(), 0);
    function<int(int)> find = [&](int x) -> int {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };
    int components = n;
    for (auto& c : connections) {
        int rx = find(c[0]), ry = find(c[1]);
        if (rx != ry) {
            if (rnk[rx] < rnk[ry]) parent[rx] = ry;
            else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
            else { parent[ry] = rx; rnk[rx]++; }
            components--;
        }
    }
    return components - 1;
}

int main() { return 0; }
