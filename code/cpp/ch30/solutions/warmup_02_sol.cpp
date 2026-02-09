/*
 * Solution: Warmup 2 — Range Min Query
 */
#include <algorithm>
#include <climits>
#include <vector>
using namespace std;
vector<int> tree_w2;
void build_w2(vector<int>& arr, int node, int s, int e) {
    if (s == e) { tree_w2[node] = arr[s]; return; }
    int m = (s + e) / 2;
    build_w2(arr, 2*node, s, m); build_w2(arr, 2*node+1, m+1, e);
    tree_w2[node] = min(tree_w2[2*node], tree_w2[2*node+1]);
}
void update_w2(int node, int s, int e, int idx, int val) {
    if (s == e) { tree_w2[node] = val; return; }
    int m = (s + e) / 2;
    if (idx <= m) update_w2(2*node, s, m, idx, val);
    else update_w2(2*node+1, m+1, e, idx, val);
    tree_w2[node] = min(tree_w2[2*node], tree_w2[2*node+1]);
}
int query_w2(int node, int s, int e, int l, int r) {
    if (r < s || e < l) return INT_MAX;
    if (l <= s && e <= r) return tree_w2[node];
    int m = (s + e) / 2;
    return min(query_w2(2*node, s, m, l, r), query_w2(2*node+1, m+1, e, l, r));
}
vector<int> solve(vector<int> arr, vector<vector<int>> queries) {
    int n = arr.size(); tree_w2.assign(4*n, INT_MAX);
    build_w2(arr, 1, 0, n-1);
    vector<int> res;
    for (auto& q : queries) {
        if (q[0] == 1) res.push_back(query_w2(1, 0, n-1, q[1], q[2]));
        else update_w2(1, 0, n-1, q[1], q[2]);
    }
    return res;
}
int main() { return 0; }
