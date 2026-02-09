/*
 * Solution for Practice 5: Satisfiability of Equality Equations
 * Chapter 29: Union-Find & Minimum Spanning Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

bool solve(vector<string>& equations) {
    vector<int> parent(26), rnk(26, 0);
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

    for (auto& eq : equations)
        if (eq[1] == '=')
            unite(eq[0] - 'a', eq[3] - 'a');

    for (auto& eq : equations)
        if (eq[1] == '!')
            if (find(eq[0] - 'a') == find(eq[3] - 'a'))
                return false;

    return true;
}

int main() { return 0; }
