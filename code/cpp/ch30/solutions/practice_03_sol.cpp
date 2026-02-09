/*
 * Solution: Practice 3 — Count in Range (Merge Sort Tree)
 */
#include <algorithm>
#include <vector>
using namespace std;
vector<vector<int>> mst;
void build_mst(vector<int>& arr, int node, int s, int e) {
    if (s == e) { mst[node] = {arr[s]}; return; }
    int m = (s + e) / 2;
    build_mst(arr, 2*node, s, m); build_mst(arr, 2*node+1, m+1, e);
    merge(mst[2*node].begin(), mst[2*node].end(),
          mst[2*node+1].begin(), mst[2*node+1].end(), back_inserter(mst[node]));
}
int query_mst(int node, int s, int e, int l, int r, int lo, int hi) {
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) {
        return (int)(upper_bound(mst[node].begin(), mst[node].end(), hi)
              - lower_bound(mst[node].begin(), mst[node].end(), lo));
    }
    int m = (s + e) / 2;
    return query_mst(2*node, s, m, l, r, lo, hi)
         + query_mst(2*node+1, m+1, e, l, r, lo, hi);
}
vector<int> solve(vector<int> arr, vector<vector<int>> queries) {
    int n = arr.size(); mst.assign(4*n, vector<int>());
    build_mst(arr, 1, 0, n-1);
    vector<int> res;
    for (auto& q : queries) res.push_back(query_mst(1, 0, n-1, q[0], q[1], q[2], q[3]));
    return res;
}
int main() { return 0; }
