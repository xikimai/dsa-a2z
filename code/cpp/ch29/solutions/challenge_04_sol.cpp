/*
 * Solution for Challenge 4: Smallest String With Swaps
 * Chapter 29: Union-Find & Minimum Spanning Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

string solve(string s, vector<vector<int>>& pairs) {
    int n = s.size();
    vector<int> parent(n), rnk(n, 0);
    iota(parent.begin(), parent.end(), 0);
    function<int(int)> find = [&](int x) -> int {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };
    auto unite = [&](int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return;
        if (rnk[rx] < rnk[ry]) parent[rx] = ry;
        else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
        else { parent[ry] = rx; rnk[rx]++; }
    };

    for (auto& p : pairs) unite(p[0], p[1]);

    map<int, vector<int>> groups;
    for (int i = 0; i < n; i++)
        groups[find(i)].push_back(i);

    string result = s;
    for (auto& [root, indices] : groups) {
        string chars;
        for (int i : indices) chars += s[i];
        sort(chars.begin(), chars.end());
        sort(indices.begin(), indices.end());
        for (int k = 0; k < (int)indices.size(); k++)
            result[indices[k]] = chars[k];
    }
    return result;
}

int main() { return 0; }
