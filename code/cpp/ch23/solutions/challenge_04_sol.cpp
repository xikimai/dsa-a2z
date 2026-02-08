/*
 * Solution for Challenge 4: House Robber III (Tree)
 * Chapter 23: Dynamic Programming I — The Foundation
 */

#include <algorithm>
#include <climits>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(vector<int> tree) {
    if (tree.empty()) return 0;
    function<pair<int,int>(int)> dfs = [&](int idx) -> pair<int,int> {
        if (idx >= (int)tree.size() || tree[idx] == -1) return {0, 0};
        auto [lr, ls] = dfs(2*idx+1);
        auto [rr, rs] = dfs(2*idx+2);
        int rob = tree[idx] + ls + rs;
        int skip = max(lr, ls) + max(rr, rs);
        return {rob, skip};
    };
    auto [r, s] = dfs(0);
    return max(r, s);
}

int main() {
    return 0;
}
