/*
 * Example 01: Segment Tree Basics — Build, Query, Update
 * Chapter 30: Segment Trees & Range Queries
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

vector<int> tree;

void build(vector<int>& arr, int node, int s, int e) {
    if (s == e) { tree[node] = arr[s]; return; }
    int m = (s + e) / 2;
    build(arr, 2*node, s, m); build(arr, 2*node+1, m+1, e);
    tree[node] = tree[2*node] + tree[2*node+1];
}

int query(int node, int s, int e, int l, int r) {
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return tree[node];
    int m = (s + e) / 2;
    return query(2*node, s, m, l, r) + query(2*node+1, m+1, e, l, r);
}

void update(int node, int s, int e, int idx, int val) {
    if (s == e) { tree[node] = val; return; }
    int m = (s + e) / 2;
    if (idx <= m) update(2*node, s, m, idx, val);
    else update(2*node+1, m+1, e, idx, val);
    tree[node] = tree[2*node] + tree[2*node+1];
}

int main() {
    vector<int> arr = {1, 3, 5, 7, 9, 11};
    int n = arr.size();
    tree.assign(4 * n, 0);
    build(arr, 1, 0, n - 1);

    cout << "Segment Tree Basics Demo" << endl;
    cout << "Sum(1,3) = " << query(1, 0, n-1, 1, 3) << endl; // 15
    update(1, 0, n-1, 1, 10);
    cout << "After update arr[1]=10:" << endl;
    cout << "Sum(1,3) = " << query(1, 0, n-1, 1, 3) << endl; // 22
    return 0;
}
