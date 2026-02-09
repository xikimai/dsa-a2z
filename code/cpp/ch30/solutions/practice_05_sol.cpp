/*
 * Solution: Practice 5 — XOR on Range
 */
#include <vector>
using namespace std;
vector<int> tree_p5;
void build_p5(vector<int>& arr, int node, int s, int e) {
    if (s == e) { tree_p5[node] = arr[s]; return; }
    int m = (s + e) / 2;
    build_p5(arr, 2*node, s, m); build_p5(arr, 2*node+1, m+1, e);
    tree_p5[node] = tree_p5[2*node] ^ tree_p5[2*node+1];
}
void update_p5(int node, int s, int e, int idx, int val) {
    if (s == e) { tree_p5[node] = val; return; }
    int m = (s + e) / 2;
    if (idx <= m) update_p5(2*node, s, m, idx, val);
    else update_p5(2*node+1, m+1, e, idx, val);
    tree_p5[node] = tree_p5[2*node] ^ tree_p5[2*node+1];
}
int query_p5(int node, int s, int e, int l, int r) {
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return tree_p5[node];
    int m = (s + e) / 2;
    return query_p5(2*node, s, m, l, r) ^ query_p5(2*node+1, m+1, e, l, r);
}
vector<int> solve(vector<int> arr, vector<vector<int>> queries) {
    int n = arr.size(); tree_p5.assign(4*n, 0);
    build_p5(arr, 1, 0, n-1);
    vector<int> res;
    for (auto& q : queries) {
        if (q[0] == 1) res.push_back(query_p5(1, 0, n-1, q[1], q[2]));
        else update_p5(1, 0, n-1, q[1], q[2]);
    }
    return res;
}
int main() { return 0; }
