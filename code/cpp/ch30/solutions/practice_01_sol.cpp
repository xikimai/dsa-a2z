/*
 * Solution: Practice 1 — Lazy Range Sum
 */
#include <vector>
using namespace std;
vector<long long> tree_p1, lazy_p1;
void pushDown_p1(int node, int s, int e) {
    if (lazy_p1[node] != 0) {
        int m = (s + e) / 2;
        tree_p1[2*node] += lazy_p1[node] * (m - s + 1);
        tree_p1[2*node+1] += lazy_p1[node] * (e - m);
        lazy_p1[2*node] += lazy_p1[node]; lazy_p1[2*node+1] += lazy_p1[node];
        lazy_p1[node] = 0;
    }
}
void rangeUpdate_p1(int node, int s, int e, int l, int r, long long val) {
    if (r < s || e < l) return;
    if (l <= s && e <= r) { tree_p1[node] += val * (e - s + 1); lazy_p1[node] += val; return; }
    pushDown_p1(node, s, e); int m = (s + e) / 2;
    rangeUpdate_p1(2*node, s, m, l, r, val); rangeUpdate_p1(2*node+1, m+1, e, l, r, val);
    tree_p1[node] = tree_p1[2*node] + tree_p1[2*node+1];
}
long long rangeQuery_p1(int node, int s, int e, int l, int r) {
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return tree_p1[node];
    pushDown_p1(node, s, e); int m = (s + e) / 2;
    return rangeQuery_p1(2*node, s, m, l, r) + rangeQuery_p1(2*node+1, m+1, e, l, r);
}
vector<long long> solve(int n, vector<vector<int>> queries) {
    tree_p1.assign(4*n, 0); lazy_p1.assign(4*n, 0);
    vector<long long> res;
    for (auto& q : queries) {
        if (q[0] == 1) rangeUpdate_p1(1, 0, n-1, q[1], q[2], q[3]);
        else res.push_back(rangeQuery_p1(1, 0, n-1, q[1], q[2]));
    }
    return res;
}
int main() { return 0; }
