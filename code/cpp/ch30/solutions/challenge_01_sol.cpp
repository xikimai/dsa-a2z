/*
 * Solution: Challenge 1 — Range Set + Range Sum
 */
#include <vector>
using namespace std;
vector<long long> tree_c1;
vector<long long> lazy_c1;
const long long NO_LAZY = -1e18;
void pushDown_c1(int node, int s, int e) {
    if (lazy_c1[node] != NO_LAZY) {
        long long val = lazy_c1[node]; int m = (s + e) / 2;
        tree_c1[2*node] = val * (m - s + 1); tree_c1[2*node+1] = val * (e - m);
        lazy_c1[2*node] = val; lazy_c1[2*node+1] = val;
        lazy_c1[node] = NO_LAZY;
    }
}
void rangeSet_c1(int node, int s, int e, int l, int r, long long val) {
    if (r < s || e < l) return;
    if (l <= s && e <= r) { tree_c1[node] = val * (e - s + 1); lazy_c1[node] = val; return; }
    pushDown_c1(node, s, e); int m = (s + e) / 2;
    rangeSet_c1(2*node, s, m, l, r, val); rangeSet_c1(2*node+1, m+1, e, l, r, val);
    tree_c1[node] = tree_c1[2*node] + tree_c1[2*node+1];
}
long long rangeQuery_c1(int node, int s, int e, int l, int r) {
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return tree_c1[node];
    pushDown_c1(node, s, e); int m = (s + e) / 2;
    return rangeQuery_c1(2*node, s, m, l, r) + rangeQuery_c1(2*node+1, m+1, e, l, r);
}
vector<long long> solve(int n, vector<vector<int>> queries) {
    tree_c1.assign(4*n, 0); lazy_c1.assign(4*n, NO_LAZY);
    vector<long long> res;
    for (auto& q : queries) {
        if (q[0] == 1) rangeSet_c1(1, 0, n-1, q[1], q[2], q[3]);
        else res.push_back(rangeQuery_c1(1, 0, n-1, q[1], q[2]));
    }
    return res;
}
int main() { return 0; }
