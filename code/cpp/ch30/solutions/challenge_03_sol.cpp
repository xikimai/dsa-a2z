/*
 * Solution: Challenge 3 — Max Subarray Sum in Range
 */
#include <algorithm>
#include <climits>
#include <vector>
using namespace std;
struct Node { long long total, prefix, suffix, best; };
vector<Node> tree_c3;
Node makeLeaf(int v) { return {v, v, v, v}; }
Node mergeNodes(Node a, Node b) {
    return {
        a.total + b.total,
        max(a.prefix, a.total + b.prefix),
        max(b.suffix, b.total + a.suffix),
        max({a.best, b.best, a.suffix + b.prefix})
    };
}
void build_c3(vector<int>& arr, int node, int s, int e) {
    if (s == e) { tree_c3[node] = makeLeaf(arr[s]); return; }
    int m = (s + e) / 2;
    build_c3(arr, 2*node, s, m); build_c3(arr, 2*node+1, m+1, e);
    tree_c3[node] = mergeNodes(tree_c3[2*node], tree_c3[2*node+1]);
}
const long long NEG_INF_C3 = LLONG_MIN / 2;
Node IDENTITY_C3 = {0, NEG_INF_C3, NEG_INF_C3, NEG_INF_C3};
Node query_c3(int node, int s, int e, int l, int r) {
    if (r < s || e < l) return IDENTITY_C3;
    if (l <= s && e <= r) return tree_c3[node];
    int m = (s + e) / 2;
    Node left = query_c3(2*node, s, m, l, r), right = query_c3(2*node+1, m+1, e, l, r);
    if (left.best == NEG_INF_C3) return right;
    if (right.best == NEG_INF_C3) return left;
    return mergeNodes(left, right);
}
vector<int> solve(vector<int> arr, vector<vector<int>> queries) {
    int n = arr.size(); tree_c3.resize(4*n);
    build_c3(arr, 1, 0, n-1);
    vector<int> res;
    for (auto& q : queries) {
        Node r = query_c3(1, 0, n-1, q[0], q[1]);
        res.push_back((int)r.best);
    }
    return res;
}
int main() { return 0; }
