/*
 * Solution: Practice 2 — Range Max with Point Update
 */
#include <algorithm>
#include <climits>
#include <vector>
using namespace std;
vector<int> tree_p2;
void build_p2(vector<int>& arr, int node, int s, int e) {
    if (s == e) { tree_p2[node] = arr[s]; return; }
    int m = (s + e) / 2;
    build_p2(arr, 2*node, s, m); build_p2(arr, 2*node+1, m+1, e);
    tree_p2[node] = max(tree_p2[2*node], tree_p2[2*node+1]);
}
void update_p2(int node, int s, int e, int idx, int val) {
    if (s == e) { tree_p2[node] = val; return; }
    int m = (s + e) / 2;
    if (idx <= m) update_p2(2*node, s, m, idx, val);
    else update_p2(2*node+1, m+1, e, idx, val);
    tree_p2[node] = max(tree_p2[2*node], tree_p2[2*node+1]);
}
int query_p2(int node, int s, int e, int l, int r) {
    if (r < s || e < l) return INT_MIN;
    if (l <= s && e <= r) return tree_p2[node];
    int m = (s + e) / 2;
    return max(query_p2(2*node, s, m, l, r), query_p2(2*node+1, m+1, e, l, r));
}
vector<int> solve(vector<int> arr, vector<vector<int>> queries) {
    int n = arr.size(); tree_p2.assign(4*n, INT_MIN);
    build_p2(arr, 1, 0, n-1);
    vector<int> res;
    for (auto& q : queries) {
        if (q[0] == 1) res.push_back(query_p2(1, 0, n-1, q[1], q[2]));
        else update_p2(1, 0, n-1, q[1], q[2]);
    }
    return res;
}
int main() { return 0; }
