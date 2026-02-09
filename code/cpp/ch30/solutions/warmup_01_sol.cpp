/*
 * Solution: Warmup 1 — Range Sum Query (Segment Tree)
 * Chapter 30: Segment Trees & Range Queries
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

vector<int> tree_w1;
void build_w1(vector<int>& arr, int node, int s, int e) {
    if (s == e) { tree_w1[node] = arr[s]; return; }
    int m = (s + e) / 2;
    build_w1(arr, 2*node, s, m); build_w1(arr, 2*node+1, m+1, e);
    tree_w1[node] = tree_w1[2*node] + tree_w1[2*node+1];
}
void update_w1(int node, int s, int e, int idx, int val) {
    if (s == e) { tree_w1[node] = val; return; }
    int m = (s + e) / 2;
    if (idx <= m) update_w1(2*node, s, m, idx, val);
    else update_w1(2*node+1, m+1, e, idx, val);
    tree_w1[node] = tree_w1[2*node] + tree_w1[2*node+1];
}
int query_w1(int node, int s, int e, int l, int r) {
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return tree_w1[node];
    int m = (s + e) / 2;
    return query_w1(2*node, s, m, l, r) + query_w1(2*node+1, m+1, e, l, r);
}
vector<int> solve(vector<int> arr, vector<vector<int>> queries) {
    int n = arr.size(); tree_w1.assign(4*n, 0);
    build_w1(arr, 1, 0, n-1);
    vector<int> res;
    for (auto& q : queries) {
        if (q[0] == 1) res.push_back(query_w1(1, 0, n-1, q[1], q[2]));
        else update_w1(1, 0, n-1, q[1], q[2]);
    }
    return res;
}
int main() { return 0; }
