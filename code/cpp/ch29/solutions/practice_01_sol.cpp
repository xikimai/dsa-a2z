/*
 * Solution for Practice 1: Number of Provinces
 * Chapter 29: Union-Find & Minimum Spanning Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& isConnected) {
    int n = isConnected.size();
    vector<int> parent(n), rnk(n, 0);
    iota(parent.begin(), parent.end(), 0);
    function<int(int)> find = [&](int x) -> int {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };
    int components = n;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (isConnected[i][j] == 1) {
                int rx = find(i), ry = find(j);
                if (rx != ry) {
                    if (rnk[rx] < rnk[ry]) parent[rx] = ry;
                    else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
                    else { parent[ry] = rx; rnk[rx]++; }
                    components--;
                }
            }
    return components;
}

int main() { return 0; }
