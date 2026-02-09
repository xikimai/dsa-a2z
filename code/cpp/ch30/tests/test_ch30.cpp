/*
 * Tests for Chapter 30: Segment Trees & Range Queries
 * Build: g++ -std=c++17 -o /tmp/test_ch30 code/cpp/ch30/tests/test_ch30.cpp && /tmp/test_ch30
 */

#include <algorithm>
#include <array>
#include <cassert>
#include <climits>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions (uniquely named with ref_ prefix)
// =====================================================================

// --- W1: Range Sum Query (Segment Tree) ---
namespace ref_w1 {
    vector<int> tree;
    void build(vector<int>& arr, int node, int s, int e) {
        if (s == e) { tree[node] = arr[s]; return; }
        int m = (s + e) / 2;
        build(arr, 2*node, s, m); build(arr, 2*node+1, m+1, e);
        tree[node] = tree[2*node] + tree[2*node+1];
    }
    void update(int node, int s, int e, int idx, int val) {
        if (s == e) { tree[node] = val; return; }
        int m = (s + e) / 2;
        if (idx <= m) update(2*node, s, m, idx, val);
        else update(2*node+1, m+1, e, idx, val);
        tree[node] = tree[2*node] + tree[2*node+1];
    }
    int query(int node, int s, int e, int l, int r) {
        if (r < s || e < l) return 0;
        if (l <= s && e <= r) return tree[node];
        int m = (s + e) / 2;
        return query(2*node, s, m, l, r) + query(2*node+1, m+1, e, l, r);
    }
}
vector<int> ref_range_sum(vector<int> arr, vector<vector<int>> queries) {
    int n = arr.size(); ref_w1::tree.assign(4*n, 0);
    ref_w1::build(arr, 1, 0, n-1);
    vector<int> res;
    for (auto& q : queries) {
        if (q[0] == 1) res.push_back(ref_w1::query(1, 0, n-1, q[1], q[2]));
        else ref_w1::update(1, 0, n-1, q[1], q[2]);
    }
    return res;
}

// --- W2: Range Min Query (Segment Tree) ---
namespace ref_w2 {
    vector<int> tree;
    void build(vector<int>& arr, int node, int s, int e) {
        if (s == e) { tree[node] = arr[s]; return; }
        int m = (s + e) / 2;
        build(arr, 2*node, s, m); build(arr, 2*node+1, m+1, e);
        tree[node] = min(tree[2*node], tree[2*node+1]);
    }
    void update(int node, int s, int e, int idx, int val) {
        if (s == e) { tree[node] = val; return; }
        int m = (s + e) / 2;
        if (idx <= m) update(2*node, s, m, idx, val);
        else update(2*node+1, m+1, e, idx, val);
        tree[node] = min(tree[2*node], tree[2*node+1]);
    }
    int query(int node, int s, int e, int l, int r) {
        if (r < s || e < l) return INT_MAX;
        if (l <= s && e <= r) return tree[node];
        int m = (s + e) / 2;
        return min(query(2*node, s, m, l, r), query(2*node+1, m+1, e, l, r));
    }
}
vector<int> ref_range_min(vector<int> arr, vector<vector<int>> queries) {
    int n = arr.size(); ref_w2::tree.assign(4*n, INT_MAX);
    ref_w2::build(arr, 1, 0, n-1);
    vector<int> res;
    for (auto& q : queries) {
        if (q[0] == 1) res.push_back(ref_w2::query(1, 0, n-1, q[1], q[2]));
        else ref_w2::update(1, 0, n-1, q[1], q[2]);
    }
    return res;
}

// --- W3: Prefix Sum with BIT ---
vector<int> ref_prefix_sum_bit(vector<int> arr, vector<vector<int>> queries) {
    int n = arr.size();
    vector<int> bit(n + 1, 0);
    auto update = [&](int i, int d) { for (i++; i <= n; i += i & (-i)) bit[i] += d; };
    auto prefix = [&](int i) -> int { int s = 0; for (i++; i > 0; i -= i & (-i)) s += bit[i]; return s; };
    for (int i = 0; i < n; i++) update(i, arr[i]);
    vector<int> res;
    for (auto& q : queries) {
        if (q[0] == 1) res.push_back(prefix(q[1]));
        else update(q[1], q[2]);
    }
    return res;
}

// --- W4: Count Inversions (BIT) ---
int ref_count_inversions(vector<int> arr) {
    if (arr.empty()) return 0;
    vector<int> sorted = arr;
    sort(sorted.begin(), sorted.end());
    sorted.erase(unique(sorted.begin(), sorted.end()), sorted.end());
    map<int,int> rank;
    for (int i = 0; i < (int)sorted.size(); i++) rank[sorted[i]] = i + 1;
    int maxR = sorted.size();
    vector<int> bit(maxR + 1, 0);
    auto update = [&](int i, int d) { for (; i <= maxR; i += i & (-i)) bit[i] += d; };
    auto prefix = [&](int i) -> int { int s = 0; for (; i > 0; i -= i & (-i)) s += bit[i]; return s; };
    int inv = 0;
    for (int i = arr.size() - 1; i >= 0; i--) {
        int r = rank[arr[i]];
        inv += prefix(r - 1);
        update(r, 1);
    }
    return inv;
}

// --- P1: Lazy Range Sum ---
namespace ref_p1 {
    vector<long long> tree, lazy;
    void pushDown(int node, int s, int e) {
        if (lazy[node] != 0) {
            int m = (s + e) / 2;
            tree[2*node] += lazy[node] * (m - s + 1);
            tree[2*node+1] += lazy[node] * (e - m);
            lazy[2*node] += lazy[node]; lazy[2*node+1] += lazy[node];
            lazy[node] = 0;
        }
    }
    void rangeUpdate(int node, int s, int e, int l, int r, long long val) {
        if (r < s || e < l) return;
        if (l <= s && e <= r) { tree[node] += val * (e - s + 1); lazy[node] += val; return; }
        pushDown(node, s, e); int m = (s + e) / 2;
        rangeUpdate(2*node, s, m, l, r, val); rangeUpdate(2*node+1, m+1, e, l, r, val);
        tree[node] = tree[2*node] + tree[2*node+1];
    }
    long long rangeQuery(int node, int s, int e, int l, int r) {
        if (r < s || e < l) return 0;
        if (l <= s && e <= r) return tree[node];
        pushDown(node, s, e); int m = (s + e) / 2;
        return rangeQuery(2*node, s, m, l, r) + rangeQuery(2*node+1, m+1, e, l, r);
    }
}
vector<long long> ref_lazy_range_sum(int n, vector<vector<int>> queries) {
    ref_p1::tree.assign(4*n, 0); ref_p1::lazy.assign(4*n, 0);
    vector<long long> res;
    for (auto& q : queries) {
        if (q[0] == 1) ref_p1::rangeUpdate(1, 0, n-1, q[1], q[2], q[3]);
        else res.push_back(ref_p1::rangeQuery(1, 0, n-1, q[1], q[2]));
    }
    return res;
}

// --- P2: Range Max with Point Update ---
namespace ref_p2 {
    vector<int> tree;
    void build(vector<int>& arr, int node, int s, int e) {
        if (s == e) { tree[node] = arr[s]; return; }
        int m = (s + e) / 2;
        build(arr, 2*node, s, m); build(arr, 2*node+1, m+1, e);
        tree[node] = max(tree[2*node], tree[2*node+1]);
    }
    void update(int node, int s, int e, int idx, int val) {
        if (s == e) { tree[node] = val; return; }
        int m = (s + e) / 2;
        if (idx <= m) update(2*node, s, m, idx, val);
        else update(2*node+1, m+1, e, idx, val);
        tree[node] = max(tree[2*node], tree[2*node+1]);
    }
    int query(int node, int s, int e, int l, int r) {
        if (r < s || e < l) return INT_MIN;
        if (l <= s && e <= r) return tree[node];
        int m = (s + e) / 2;
        return max(query(2*node, s, m, l, r), query(2*node+1, m+1, e, l, r));
    }
}
vector<int> ref_range_max(vector<int> arr, vector<vector<int>> queries) {
    int n = arr.size(); ref_p2::tree.assign(4*n, INT_MIN);
    ref_p2::build(arr, 1, 0, n-1);
    vector<int> res;
    for (auto& q : queries) {
        if (q[0] == 1) res.push_back(ref_p2::query(1, 0, n-1, q[1], q[2]));
        else ref_p2::update(1, 0, n-1, q[1], q[2]);
    }
    return res;
}

// --- P3: Count in Range (Merge Sort Tree) ---
namespace ref_p3 {
    vector<vector<int>> mst;
    void build(vector<int>& arr, int node, int s, int e) {
        if (s == e) { mst[node] = {arr[s]}; return; }
        int m = (s + e) / 2;
        build(arr, 2*node, s, m); build(arr, 2*node+1, m+1, e);
        merge(mst[2*node].begin(), mst[2*node].end(),
              mst[2*node+1].begin(), mst[2*node+1].end(), back_inserter(mst[node]));
    }
    int query(int node, int s, int e, int l, int r, int lo, int hi) {
        if (r < s || e < l) return 0;
        if (l <= s && e <= r) {
            return (int)(upper_bound(mst[node].begin(), mst[node].end(), hi)
                  - lower_bound(mst[node].begin(), mst[node].end(), lo));
        }
        int m = (s + e) / 2;
        return query(2*node, s, m, l, r, lo, hi)
             + query(2*node+1, m+1, e, l, r, lo, hi);
    }
}
vector<int> ref_count_in_range(vector<int> arr, vector<vector<int>> queries) {
    int n = arr.size(); ref_p3::mst.assign(4*n, vector<int>());
    ref_p3::build(arr, 1, 0, n-1);
    vector<int> res;
    for (auto& q : queries) res.push_back(ref_p3::query(1, 0, n-1, q[0], q[1], q[2], q[3]));
    return res;
}

// --- P4: Kth Order Statistics ---
namespace ref_p4 {
    const int MAX_VAL = 100001;
    int tree[4 * 100001];
    void update(int node, int s, int e, int idx, int d) {
        if (s == e) { tree[node] += d; return; }
        int m = (s + e) / 2;
        if (idx <= m) update(2*node, s, m, idx, d);
        else update(2*node+1, m+1, e, idx, d);
        tree[node] = tree[2*node] + tree[2*node+1];
    }
    int kth(int node, int s, int e, int k) {
        if (s == e) return s;
        int m = (s + e) / 2;
        if (tree[2*node] >= k) return kth(2*node, s, m, k);
        return kth(2*node+1, m+1, e, k - tree[2*node]);
    }
}
vector<int> ref_kth_order(vector<vector<int>> queries) {
    memset(ref_p4::tree, 0, sizeof(ref_p4::tree));
    vector<int> res;
    for (auto& q : queries) {
        if (q[0] == 1) ref_p4::update(1, 1, ref_p4::MAX_VAL-1, q[1], 1);
        else if (q[0] == 2) ref_p4::update(1, 1, ref_p4::MAX_VAL-1, q[1], -1);
        else res.push_back(ref_p4::kth(1, 1, ref_p4::MAX_VAL-1, q[1]));
    }
    return res;
}

// --- P5: XOR on Range ---
namespace ref_p5 {
    vector<int> tree;
    void build(vector<int>& arr, int node, int s, int e) {
        if (s == e) { tree[node] = arr[s]; return; }
        int m = (s + e) / 2;
        build(arr, 2*node, s, m); build(arr, 2*node+1, m+1, e);
        tree[node] = tree[2*node] ^ tree[2*node+1];
    }
    void update(int node, int s, int e, int idx, int val) {
        if (s == e) { tree[node] = val; return; }
        int m = (s + e) / 2;
        if (idx <= m) update(2*node, s, m, idx, val);
        else update(2*node+1, m+1, e, idx, val);
        tree[node] = tree[2*node] ^ tree[2*node+1];
    }
    int query(int node, int s, int e, int l, int r) {
        if (r < s || e < l) return 0;
        if (l <= s && e <= r) return tree[node];
        int m = (s + e) / 2;
        return query(2*node, s, m, l, r) ^ query(2*node+1, m+1, e, l, r);
    }
}
vector<int> ref_xor_range(vector<int> arr, vector<vector<int>> queries) {
    int n = arr.size(); ref_p5::tree.assign(4*n, 0);
    ref_p5::build(arr, 1, 0, n-1);
    vector<int> res;
    for (auto& q : queries) {
        if (q[0] == 1) res.push_back(ref_p5::query(1, 0, n-1, q[1], q[2]));
        else ref_p5::update(1, 0, n-1, q[1], q[2]);
    }
    return res;
}

// --- C1: Range Set + Range Sum (Lazy) ---
namespace ref_c1 {
    vector<long long> tree;
    vector<long long> lazy;
    const long long NO_LAZY = -1e18;
    void pushDown(int node, int s, int e) {
        if (lazy[node] != NO_LAZY) {
            long long val = lazy[node]; int m = (s + e) / 2;
            tree[2*node] = val * (m - s + 1); tree[2*node+1] = val * (e - m);
            lazy[2*node] = val; lazy[2*node+1] = val;
            lazy[node] = NO_LAZY;
        }
    }
    void rangeSet(int node, int s, int e, int l, int r, long long val) {
        if (r < s || e < l) return;
        if (l <= s && e <= r) { tree[node] = val * (e - s + 1); lazy[node] = val; return; }
        pushDown(node, s, e); int m = (s + e) / 2;
        rangeSet(2*node, s, m, l, r, val); rangeSet(2*node+1, m+1, e, l, r, val);
        tree[node] = tree[2*node] + tree[2*node+1];
    }
    long long rangeQuery(int node, int s, int e, int l, int r) {
        if (r < s || e < l) return 0;
        if (l <= s && e <= r) return tree[node];
        pushDown(node, s, e); int m = (s + e) / 2;
        return rangeQuery(2*node, s, m, l, r) + rangeQuery(2*node+1, m+1, e, l, r);
    }
}
vector<long long> ref_range_set_sum(int n, vector<vector<int>> queries) {
    ref_c1::tree.assign(4*n, 0); ref_c1::lazy.assign(4*n, ref_c1::NO_LAZY);
    vector<long long> res;
    for (auto& q : queries) {
        if (q[0] == 1) ref_c1::rangeSet(1, 0, n-1, q[1], q[2], q[3]);
        else res.push_back(ref_c1::rangeQuery(1, 0, n-1, q[1], q[2]));
    }
    return res;
}

// --- C2: Distinct Values in Range (Offline + BIT) ---
vector<int> ref_distinct_in_range(vector<int> arr, vector<vector<int>> queries) {
    int n = arr.size();
    vector<int> bit(n + 2, 0);
    auto update = [&](int i, int d) { for (i++; i <= n; i += i & (-i)) bit[i] += d; };
    auto prefix = [&](int i) -> int { int s = 0; for (i++; i > 0; i -= i & (-i)) s += bit[i]; return s; };

    vector<array<int,3>> indexed(queries.size());
    for (int i = 0; i < (int)queries.size(); i++) { indexed[i] = {queries[i][0], queries[i][1], i}; }
    sort(indexed.begin(), indexed.end(), [](auto& a, auto& b) { return a[1] < b[1]; });

    vector<int> results(queries.size());
    unordered_map<int,int> lastSeen;
    int j = 0;
    for (auto& q : indexed) {
        int l = q[0], r = q[1], origIdx = q[2];
        while (j <= r) {
            int val = arr[j];
            if (lastSeen.count(val)) update(lastSeen[val], -1);
            lastSeen[val] = j; update(j, 1); j++;
        }
        results[origIdx] = prefix(r) - (l > 0 ? prefix(l - 1) : 0);
    }
    return results;
}

// --- C3: Max Subarray Sum in Range ---
namespace ref_c3 {
    struct Node { long long total, prefix, suffix, best; };
    vector<Node> tree;
    Node makeLeaf(int v) { return {v, v, v, v}; }
    Node mergeNodes(Node a, Node b) {
        return {
            a.total + b.total,
            max(a.prefix, a.total + b.prefix),
            max(b.suffix, b.total + a.suffix),
            max({a.best, b.best, a.suffix + b.prefix})
        };
    }
    void build(vector<int>& arr, int node, int s, int e) {
        if (s == e) { tree[node] = makeLeaf(arr[s]); return; }
        int m = (s + e) / 2;
        build(arr, 2*node, s, m); build(arr, 2*node+1, m+1, e);
        tree[node] = mergeNodes(tree[2*node], tree[2*node+1]);
    }
    const long long NEG_INF = LLONG_MIN / 2;
    Node IDENTITY = {0, NEG_INF, NEG_INF, NEG_INF};
    Node query(int node, int s, int e, int l, int r) {
        if (r < s || e < l) return IDENTITY;
        if (l <= s && e <= r) return tree[node];
        int m = (s + e) / 2;
        Node left = query(2*node, s, m, l, r), right = query(2*node+1, m+1, e, l, r);
        if (left.best == NEG_INF) return right;
        if (right.best == NEG_INF) return left;
        return mergeNodes(left, right);
    }
}
vector<int> ref_max_subarray_range(vector<int> arr, vector<vector<int>> queries) {
    int n = arr.size(); ref_c3::tree.resize(4*n);
    ref_c3::build(arr, 1, 0, n-1);
    vector<int> res;
    for (auto& q : queries) {
        ref_c3::Node r = ref_c3::query(1, 0, n-1, q[0], q[1]);
        res.push_back((int)r.best);
    }
    return res;
}

// --- C4: Interval Scheduling ---
int ref_interval_scheduling(vector<vector<int>> intervals) {
    if (intervals.empty()) return 0;
    sort(intervals.begin(), intervals.end(), [](auto& a, auto& b) { return a[1] < b[1]; });
    int count = 1, lastEnd = intervals[0][1];
    for (int i = 1; i < (int)intervals.size(); i++) {
        if (intervals[i][0] >= lastEnd) { count++; lastEnd = intervals[i][1]; }
    }
    return count;
}

// =====================================================================
// Test runner
// =====================================================================

int passed = 0, failed_count = 0;

void check(int expected, int actual, const string& msg) {
    if (expected == actual) { passed++; }
    else { failed_count++; cout << "FAIL: " << msg << " -- expected " << expected << ", got " << actual << endl; }
}

void check_long(long long expected, long long actual, const string& msg) {
    if (expected == actual) { passed++; }
    else { failed_count++; cout << "FAIL: " << msg << " -- expected " << expected << ", got " << actual << endl; }
}

void check_vec(vector<int> expected, vector<int> actual, const string& msg) {
    if (expected == actual) { passed++; }
    else {
        failed_count++;
        cout << "FAIL: " << msg << " -- expected [";
        for (int i = 0; i < (int)expected.size(); i++) cout << (i?",":"") << expected[i];
        cout << "], got [";
        for (int i = 0; i < (int)actual.size(); i++) cout << (i?",":"") << actual[i];
        cout << "]" << endl;
    }
}

void check_vec_long(vector<long long> expected, vector<long long> actual, const string& msg) {
    if (expected == actual) { passed++; }
    else {
        failed_count++;
        cout << "FAIL: " << msg << " -- expected [";
        for (int i = 0; i < (int)expected.size(); i++) cout << (i?",":"") << expected[i];
        cout << "], got [";
        for (int i = 0; i < (int)actual.size(); i++) cout << (i?",":"") << actual[i];
        cout << "]" << endl;
    }
}

int main() {
    cout << "Chapter 30: Segment Trees & Range Queries" << endl;
    cout << "================================================================" << endl << endl;

    // ---- W1: Range Sum Query ----
    check_vec({15, 22}, ref_range_sum({1,3,5,7,9,11}, {{1,1,3},{2,1,10},{1,1,3}}), "W1: basic sum + update");
    check_vec({15, 22}, ref_range_sum({1,2,3,4,5}, {{1,0,4},{2,2,10},{1,0,4}}), "W1: full range");
    check_vec({5, 3}, ref_range_sum({5}, {{1,0,0},{2,0,3},{1,0,0}}), "W1: single element");
    check_vec({6, 2}, ref_range_sum({1,2,3}, {{1,0,2},{1,1,1}}), "W1: no updates");

    // ---- W2: Range Min Query ----
    check_vec({1, 2}, ref_range_min({2,5,1,4,9,3}, {{1,0,5},{2,2,8},{1,0,5}}), "W2: basic min + update");
    check_vec({1, 2}, ref_range_min({7,3,8,1,6}, {{1,1,3},{2,3,2},{1,1,3}}), "W2: update changes min");
    check_vec({5, 2}, ref_range_min({5}, {{1,0,0},{2,0,2},{1,0,0}}), "W2: single element");

    // ---- W3: Prefix Sum with BIT ----
    check_vec({10, 15}, ref_prefix_sum_bit({1,2,3,4,5}, {{1,3,0},{2,2,5},{1,3,0}}), "W3: basic prefix + add");
    check_vec({14, 16}, ref_prefix_sum_bit({3,1,4,1,5}, {{1,4,0},{2,0,2},{1,4,0}}), "W3: with add");
    check_vec({7, 10}, ref_prefix_sum_bit({7}, {{1,0,0},{2,0,3},{1,0,0}}), "W3: single");

    // ---- W4: Count Inversions ----
    check(5, ref_count_inversions({2,3,8,6,1}), "W4: mixed");
    check(10, ref_count_inversions({5,4,3,2,1}), "W4: reverse sorted");
    check(0, ref_count_inversions({1,2,3,4,5}), "W4: sorted");
    check(0, ref_count_inversions({1,1,1}), "W4: all same");
    check(0, ref_count_inversions({}), "W4: empty");

    // ---- P1: Lazy Range Sum ----
    check_vec_long({15, 15}, ref_lazy_range_sum(5, {{1,0,4,3},{2,0,4},{1,1,3,2},{2,1,3}}), "P1: basic lazy");
    check_vec_long({15, 15}, ref_lazy_range_sum(3, {{1,0,2,5},{2,0,2},{1,0,0,10},{2,0,0}}), "P1: add then query");
    check_vec_long({7}, ref_lazy_range_sum(1, {{1,0,0,7},{2,0,0}}), "P1: single element");

    // ---- P2: Range Max Query ----
    check_vec({9, 6}, ref_range_max({3,1,4,1,5,9,2,6}, {{1,0,7},{2,5,1},{1,0,7}}), "P2: basic max + update");
    check_vec({3, 5}, ref_range_max({1,2,3}, {{1,0,2},{2,1,5},{1,0,2}}), "P2: small");
    check_vec({10, 20}, ref_range_max({10}, {{1,0,0},{2,0,20},{1,0,0}}), "P2: single");

    // ---- P3: Count in Range (Merge Sort Tree) ----
    check_vec({5, 3, 3}, ref_count_in_range({1,3,5,7,9,2,4,6},
        {{0,7,3,7},{0,3,1,5},{2,5,5,9}}), "P3: basic count");
    check_vec({1}, ref_count_in_range({10,20,30}, {{0,2,15,25}}), "P3: single match");
    check_vec({0}, ref_count_in_range({1,2,3}, {{0,2,10,20}}), "P3: no match");
    check_vec({3}, ref_count_in_range({5,5,5}, {{0,2,5,5}}), "P3: all match");

    // ---- P4: Kth Order Statistics ----
    check_vec({3, 5}, ref_kth_order({{1,5},{1,3},{1,7},{1,1},{3,2},{2,3},{3,2}}), "P4: basic kth");
    check_vec({10}, ref_kth_order({{1,10},{3,1}}), "P4: single");
    check_vec({5, 5, 5}, ref_kth_order({{1,5},{1,5},{3,1},{3,2},{2,5},{3,1}}), "P4: duplicates");

    // ---- P5: XOR on Range ----
    check_vec({1, 5}, ref_xor_range({1,2,3,4,5}, {{1,0,4},{2,2,7},{1,0,4}}), "P5: basic xor + update");
    check_vec({6, 3}, ref_xor_range({3,5}, {{1,0,1},{2,0,6},{1,0,1}}), "P5: small");
    check_vec({42}, ref_xor_range({42}, {{1,0,0}}), "P5: single");

    // ---- C1: Range Set + Range Sum ----
    check_vec_long({15, 21}, ref_range_set_sum(5, {{1,0,4,3},{2,0,4},{1,1,3,5},{2,0,4}}), "C1: basic set + sum");
    check_vec_long({30, 20}, ref_range_set_sum(3, {{1,0,2,10},{2,0,2},{1,1,1,0},{2,0,2}}), "C1: overwrite");
    check_vec_long({7, 3}, ref_range_set_sum(1, {{1,0,0,7},{2,0,0},{1,0,0,3},{2,0,0}}), "C1: single");

    // ---- C2: Distinct Values in Range ----
    check_vec({3, 2, 3}, ref_distinct_in_range({1,2,1,3,2,1}, {{0,5},{0,2},{3,5}}), "C2: basic distinct");
    check_vec({1}, ref_distinct_in_range({1,1,1}, {{0,2}}), "C2: all same");
    check_vec({4, 2}, ref_distinct_in_range({1,2,3,4}, {{0,3},{1,2}}), "C2: all distinct");
    check_vec({1}, ref_distinct_in_range({5}, {{0,0}}), "C2: single");

    // ---- C3: Max Subarray Sum in Range ----
    check_vec({8, 8, 7}, ref_max_subarray_range({1,-2,3,4,-1,2,-5,3},
        {{0,7},{2,5},{0,3}}), "C3: basic max subarray");
    check_vec({-1}, ref_max_subarray_range({-1,-2,-3}, {{0,2}}), "C3: all negative");
    check_vec({5}, ref_max_subarray_range({5}, {{0,0}}), "C3: single");
    check_vec({-5}, ref_max_subarray_range({-5}, {{0,0}}), "C3: negative single");

    // ---- C4: Interval Scheduling ----
    check(2, ref_interval_scheduling({{1,3},{2,5},{4,7},{6,9}}), "C4: overlapping");
    check(4, ref_interval_scheduling({{1,2},{2,3},{3,4},{4,5}}), "C4: non-overlapping");
    check(3, ref_interval_scheduling({{1,10},{2,3},{4,5},{6,7}}), "C4: one large");
    check(1, ref_interval_scheduling({{1,5}}), "C4: single");
    check(0, ref_interval_scheduling({}), "C4: empty");

    cout << endl;
    if (failed_count == 0) {
        printf("All %d ch30 C++ tests passed!\n", passed);
    } else {
        printf("%d passed, %d failed.\n", passed, failed_count);
        return 1;
    }
    return 0;
}
