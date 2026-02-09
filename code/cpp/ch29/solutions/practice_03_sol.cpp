/*
 * Solution for Practice 3: Most Stones Removed
 * Chapter 29: Union-Find & Minimum Spanning Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& stones) {
    if (stones.empty()) return 0;
    unordered_map<int, int> parent, rnk;
    function<int(int)> find = [&](int x) -> int {
        if (parent.find(x) == parent.end()) { parent[x] = x; rnk[x] = 0; }
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };
    auto unite = [&](int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return;
        if (rnk[rx] < rnk[ry]) parent[rx] = ry;
        else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
        else { parent[ry] = rx; rnk[rx]++; }
    };
    for (auto& s : stones)
        unite(s[0], s[1] + 10001);
    unordered_set<int> components;
    for (auto& s : stones)
        components.insert(find(s[0]));
    return (int)stones.size() - (int)components.size();
}

int main() { return 0; }
