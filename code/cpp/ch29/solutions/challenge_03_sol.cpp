/*
 * Solution for Challenge 3: Number of Islands II
 * Chapter 29: Union-Find & Minimum Spanning Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> solve(int m, int n, vector<vector<int>>& positions) {
    vector<int> parent(m * n, -1), rnk(m * n, 0);
    function<int(int)> find = [&](int x) -> int {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };

    int count = 0;
    vector<int> result;
    int dirs[][2] = {{-1,0},{1,0},{0,-1},{0,1}};

    for (auto& pos : positions) {
        int r = pos[0], c = pos[1];
        int idx = r * n + c;
        if (parent[idx] != -1) { // duplicate
            result.push_back(count);
            continue;
        }
        parent[idx] = idx;
        count++;
        for (auto& d : dirs) {
            int nr = r + d[0], nc = c + d[1];
            int nidx = nr * n + nc;
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && parent[nidx] != -1) {
                int rx = find(idx), ry = find(nidx);
                if (rx != ry) {
                    if (rnk[rx] < rnk[ry]) parent[rx] = ry;
                    else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
                    else { parent[ry] = rx; rnk[rx]++; }
                    count--;
                }
            }
        }
        result.push_back(count);
    }
    return result;
}

int main() { return 0; }
