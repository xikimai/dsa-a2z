/*
 * Solution: Practice 4 — Kth Order Statistics
 */
#include <vector>
using namespace std;
const int MAX_VAL = 100001;
int tree_p4[4 * MAX_VAL];
void update_p4(int node, int s, int e, int idx, int d) {
    if (s == e) { tree_p4[node] += d; return; }
    int m = (s + e) / 2;
    if (idx <= m) update_p4(2*node, s, m, idx, d);
    else update_p4(2*node+1, m+1, e, idx, d);
    tree_p4[node] = tree_p4[2*node] + tree_p4[2*node+1];
}
int kth_p4(int node, int s, int e, int k) {
    if (s == e) return s;
    int m = (s + e) / 2;
    if (tree_p4[2*node] >= k) return kth_p4(2*node, s, m, k);
    return kth_p4(2*node+1, m+1, e, k - tree_p4[2*node]);
}
vector<int> solve(vector<vector<int>> queries) {
    fill(tree_p4, tree_p4 + 4 * MAX_VAL, 0);
    vector<int> res;
    for (auto& q : queries) {
        if (q[0] == 1) update_p4(1, 1, MAX_VAL-1, q[1], 1);
        else if (q[0] == 2) update_p4(1, 1, MAX_VAL-1, q[1], -1);
        else res.push_back(kth_p4(1, 1, MAX_VAL-1, q[1]));
    }
    return res;
}
int main() { return 0; }
