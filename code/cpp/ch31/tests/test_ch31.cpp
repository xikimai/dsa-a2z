/*
 * Tests for Chapter 31: Advanced DP — Bitmask, Interval, Trees
 * Build: g++ -std=c++17 -o /tmp/test_ch31 code/cpp/ch31/tests/test_ch31.cpp && /tmp/test_ch31
 */

#include <algorithm>
#include <array>
#include <cassert>
#include <climits>
#include <functional>
#include <iostream>
#include <map>
#include <stack>
#include <string>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions (uniquely named with ref_ prefix)
// =====================================================================

// W1: TSP — bitmask DP
int ref_tsp(int n, vector<vector<int>> dist) {
    int INF = INT_MAX / 2;
    int full = (1 << n) - 1;
    vector<vector<int>> dp(1 << n, vector<int>(n, INF));
    dp[1][0] = 0;
    for (int mask = 1; mask <= full; mask++)
        for (int u = 0; u < n; u++) {
            if (dp[mask][u] >= INF) continue;
            if (!(mask & (1 << u))) continue;
            for (int v = 0; v < n; v++) {
                if (mask & (1 << v)) continue;
                int nm = mask | (1 << v);
                dp[nm][v] = min(dp[nm][v], dp[mask][u] + dist[u][v]);
            }
        }
    int ans = INF;
    for (int u = 0; u < n; u++) ans = min(ans, dp[full][u] + dist[u][0]);
    return ans;
}

// W2: MCM — interval DP
int ref_mcm(vector<int> dims) {
    int n = dims.size() - 1;
    if (n <= 1) return 0;
    vector<vector<int>> dp(n, vector<int>(n, 0));
    for (int len = 2; len <= n; len++)
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            dp[i][j] = INT_MAX;
            for (int k = i; k < j; k++)
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + dims[i]*dims[k+1]*dims[j+1]);
        }
    return dp[0][n - 1];
}

// W3: House Robber on Tree — tree DP
int ref_house_robber_tree(int n, vector<int> values, vector<vector<int>> edges) {
    if (n == 0) return 0;
    if (n == 1) return values[0];
    vector<vector<int>> adj(n);
    for (auto& e : edges) { adj[e[0]].push_back(e[1]); adj[e[1]].push_back(e[0]); }
    vector<array<int,2>> dp(n, {0, 0});
    vector<bool> visited(n, false);
    vector<int> par(n, -1), order;
    stack<int> stk;
    stk.push(0);
    while (!stk.empty()) {
        int u = stk.top(); stk.pop();
        if (visited[u]) continue;
        visited[u] = true;
        order.push_back(u);
        for (int v : adj[u]) if (!visited[v]) { par[v] = u; stk.push(v); }
    }
    for (int idx = order.size() - 1; idx >= 0; idx--) {
        int u = order[idx];
        dp[u][1] = values[u];
        for (int v : adj[u]) {
            if (v == par[u]) continue;
            dp[u][0] += max(dp[v][0], dp[v][1]);
            dp[u][1] += dp[v][0];
        }
    }
    return max(dp[0][0], dp[0][1]);
}

// P1: Shortest Hamiltonian Path
int ref_hamiltonian_path(int n, vector<vector<int>> dist) {
    int INF = INT_MAX / 2;
    int full = (1 << n) - 1;
    vector<vector<int>> dp(1 << n, vector<int>(n, INF));
    for (int i = 0; i < n; i++) dp[1 << i][i] = 0;
    for (int mask = 1; mask <= full; mask++)
        for (int u = 0; u < n; u++) {
            if (dp[mask][u] >= INF) continue;
            if (!(mask & (1 << u))) continue;
            for (int v = 0; v < n; v++) {
                if (mask & (1 << v)) continue;
                int nm = mask | (1 << v);
                dp[nm][v] = min(dp[nm][v], dp[mask][u] + dist[u][v]);
            }
        }
    int ans = INF;
    for (int u = 0; u < n; u++) ans = min(ans, dp[full][u]);
    return ans;
}

// P2: Burst Balloons
int ref_burst_balloons(vector<int> nums) {
    int n = nums.size() + 2;
    vector<int> vals(n);
    vals[0] = vals[n - 1] = 1;
    for (int i = 0; i < (int)nums.size(); i++) vals[i + 1] = nums[i];
    vector<vector<int>> dp(n, vector<int>(n, 0));
    for (int len = 1; len <= n - 2; len++)
        for (int left = 1; left < n - len; left++) {
            int right = left + len - 1;
            for (int k = left; k <= right; k++) {
                int coins = vals[left-1]*vals[k]*vals[right+1] + dp[left][k-1] + dp[k+1][right];
                dp[left][right] = max(dp[left][right], coins);
            }
        }
    return dp[1][n - 2];
}

// P3: Min Score Triangulation
int ref_triangulation(vector<int> values) {
    int n = values.size();
    if (n < 3) return 0;
    vector<vector<int>> dp(n, vector<int>(n, 0));
    for (int len = 3; len <= n; len++)
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            dp[i][j] = INT_MAX;
            for (int k = i + 1; k < j; k++)
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + values[i]*values[k]*values[j]);
        }
    return dp[0][n - 1];
}

// P4: Tree Diameter
int ref_tree_diameter(int n, vector<vector<int>> edges) {
    if (n <= 1) return 0;
    vector<vector<int>> adj(n);
    for (auto& e : edges) { adj[e[0]].push_back(e[1]); adj[e[1]].push_back(e[0]); }
    vector<int> depth(n, 0), par(n, -1);
    vector<bool> visited(n, false);
    vector<int> order;
    stack<int> stk;
    stk.push(0);
    while (!stk.empty()) {
        int u = stk.top(); stk.pop();
        if (visited[u]) continue;
        visited[u] = true;
        order.push_back(u);
        for (int v : adj[u]) if (!visited[v]) { par[v] = u; stk.push(v); }
    }
    int diameter = 0;
    for (int idx = order.size() - 1; idx >= 0; idx--) {
        int u = order[idx];
        int top1 = 0, top2 = 0;
        for (int v : adj[u]) {
            if (v == par[u]) continue;
            int d = depth[v] + 1;
            if (d >= top1) { top2 = top1; top1 = d; }
            else if (d > top2) top2 = d;
        }
        depth[u] = top1;
        diameter = max(diameter, top1 + top2);
    }
    return diameter;
}

// P5: Unique Digits
int dig_arr[10]; int dig_len;
map<long long, int> dig_memo;
int dig_dp(int pos, bool tight, int mask, bool started) {
    if (pos == dig_len) return started ? 1 : 0;
    long long key = ((long long)pos << 13) | ((tight?1LL:0LL) << 12) | ((long long)mask << 1) | (started?1LL:0LL);
    auto it = dig_memo.find(key);
    if (it != dig_memo.end()) return it->second;
    int limit = tight ? dig_arr[pos] : 9;
    int count = 0;
    for (int d = 0; d <= limit; d++) {
        if (started && (mask & (1 << d))) continue;
        bool nt = tight && (d == limit);
        bool ns = started || (d != 0);
        int nm = ns ? (mask | (1 << d)) : mask;
        count += dig_dp(pos + 1, nt, nm, ns);
    }
    dig_memo[key] = count;
    return count;
}
int ref_unique_digits(int n) {
    string s = to_string(n);
    dig_len = s.size();
    for (int i = 0; i < dig_len; i++) dig_arr[i] = s[i] - '0';
    dig_memo.clear();
    return dig_dp(0, true, 0, false);
}

// C1: Merge Stones
int ref_merge_stones(vector<int> stones, int k) {
    int n = stones.size();
    if ((n - 1) % (k - 1) != 0) return -1;
    if (n == 1) return 0;
    vector<int> prefix(n + 1, 0);
    for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + stones[i];
    int INF = INT_MAX / 2;
    vector<vector<int>> dp(n, vector<int>(n, 0));
    for (int len = 2; len <= n; len++)
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            dp[i][j] = INF;
            for (int mid = i; mid < j; mid += k - 1)
                dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j]);
            if ((j - i) % (k - 1) == 0)
                dp[i][j] += prefix[j + 1] - prefix[i];
        }
    return dp[0][n - 1];
}

// C2: Wear Hats
int ref_wear_hats(int n, vector<vector<int>> hats) {
    const int MOD = 1e9 + 7;
    vector<vector<int>> h2p(41);
    for (int p = 0; p < n; p++) for (int h : hats[p]) h2p[h].push_back(p);
    int full = (1 << n) - 1;
    vector<long long> dp(1 << n, 0);
    dp[0] = 1;
    for (int hat = 1; hat <= 40; hat++) {
        vector<long long> nd(dp);
        for (int mask = 0; mask <= full; mask++) {
            if (dp[mask] == 0) continue;
            for (int p : h2p[hat]) {
                if (mask & (1 << p)) continue;
                nd[mask | (1 << p)] = (nd[mask | (1 << p)] + dp[mask]) % MOD;
            }
        }
        dp = nd;
    }
    return (int)dp[full];
}

// C3: Binary Tree Cameras
int ref_cameras(int n, vector<vector<int>> edges) {
    if (n == 0) return 0;
    if (n <= 2) return 1;
    const int INF2 = 1000000;
    vector<vector<int>> adj(n);
    for (auto& e : edges) { adj[e[0]].push_back(e[1]); adj[e[1]].push_back(e[0]); }
    vector<array<int,3>> dp(n, {0, 0, 0});
    vector<bool> visited(n, false);
    vector<int> par(n, -1), order;
    stack<int> stk;
    stk.push(0);
    while (!stk.empty()) {
        int u = stk.top(); stk.pop();
        if (visited[u]) continue;
        visited[u] = true;
        order.push_back(u);
        for (int v : adj[u]) if (!visited[v]) { par[v] = u; stk.push(v); }
    }
    for (int idx = order.size() - 1; idx >= 0; idx--) {
        int u = order[idx];
        vector<int> ch;
        for (int v : adj[u]) if (v != par[u]) ch.push_back(v);
        if (ch.empty()) { dp[u] = {0, INF2, 1}; continue; }
        int cam = 1;
        for (int v : ch) cam += min({dp[v][0], dp[v][1], dp[v][2]});
        int nc = 0;
        for (int v : ch) nc += min(dp[v][1], dp[v][2]);
        int base = 0;
        for (int v : ch) base += min(dp[v][1], dp[v][2]);
        int cov = INF2;
        bool all1 = true;
        for (int v : ch) if (dp[v][2] <= dp[v][1]) { all1 = false; break; }
        if (!all1) cov = base;
        else { int mu = INF2; for (int v : ch) mu = min(mu, dp[v][2]-dp[v][1]); cov = base + mu; }
        dp[u] = {nc, cov, cam};
    }
    return min(dp[0][1], dp[0][2]);
}

// C4: Palindrome Partitioning II
int ref_palindrome_partition(string s) {
    int n = s.size();
    if (n <= 1) return 0;
    vector<vector<bool>> isPal(n, vector<bool>(n, false));
    for (int i = 0; i < n; i++) isPal[i][i] = true;
    for (int i = 0; i < n - 1; i++) isPal[i][i+1] = (s[i] == s[i+1]);
    for (int len = 3; len <= n; len++)
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            isPal[i][j] = (s[i] == s[j]) && isPal[i+1][j-1];
        }
    vector<int> dp(n);
    for (int i = 0; i < n; i++) {
        if (isPal[0][i]) dp[i] = 0;
        else { dp[i] = i; for (int j = 1; j <= i; j++) if (isPal[j][i]) dp[i] = min(dp[i], dp[j-1]+1); }
    }
    return dp[n - 1];
}

// =====================================================================
// Test runner
// =====================================================================

int passed = 0, failed_count = 0;

void check(int expected, int actual, const string& msg) {
    if (expected == actual) { passed++; }
    else { failed_count++; cout << "FAIL: " << msg << " — expected " << expected << ", got " << actual << endl; }
}

int main() {
    cout << "Chapter 31: Advanced DP — Bitmask, Interval, Trees" << endl;
    cout << "================================================================" << endl << endl;

    // W1: TSP
    check(80, ref_tsp(4, {{0,10,15,20},{10,0,35,25},{15,35,0,30},{20,25,30,0}}), "W1: four cities");
    check(23, ref_tsp(3, {{0,1,15},{1,0,7},{15,7,0}}), "W1: three cities");
    check(10, ref_tsp(2, {{0,5},{5,0}}), "W1: two cities");
    check(4, ref_tsp(4, {{0,1,1,1},{1,0,1,1},{1,1,0,1},{1,1,1,0}}), "W1: symmetric");

    // W2: MCM
    check(4500, ref_mcm({10,30,5,60}), "W2: three matrices");
    check(26000, ref_mcm({40,20,30,10,30}), "W2: four matrices");
    check(6000, ref_mcm({10,20,30}), "W2: two matrices");
    check(0, ref_mcm({5,10}), "W2: single matrix");

    // W3: House Robber Tree
    check(7, ref_house_robber_tree(4, {1,2,3,4}, {{0,1},{0,2},{1,3}}), "W3: four nodes");
    check(8, ref_house_robber_tree(3, {1,3,5}, {{0,1},{0,2}}), "W3: three nodes");
    check(10, ref_house_robber_tree(1, {10}, {}), "W3: single");
    check(10, ref_house_robber_tree(4, {3,4,5,6}, {{0,1},{1,2},{2,3}}), "W3: chain");

    // P1: Hamiltonian Path
    check(50, ref_hamiltonian_path(4, {{0,10,15,20},{10,0,35,25},{15,35,0,30},{20,25,30,0}}), "P1: four cities");
    check(8, ref_hamiltonian_path(3, {{0,1,15},{1,0,7},{15,7,0}}), "P1: three cities");
    check(5, ref_hamiltonian_path(2, {{0,5},{5,0}}), "P1: two cities");

    // P2: Burst Balloons
    check(167, ref_burst_balloons({3,1,5,8}), "P2: four balloons");
    check(10, ref_burst_balloons({1,5}), "P2: two balloons");
    check(7, ref_burst_balloons({7}), "P2: single");

    // P3: Triangulation
    check(6, ref_triangulation({1,2,3}), "P3: triangle");
    check(144, ref_triangulation({3,7,4,5}), "P3: square");
    check(13, ref_triangulation({1,3,1,4,1,5}), "P3: hexagon");

    // P4: Tree Diameter
    check(3, ref_tree_diameter(5, {{0,1},{1,2},{1,3},{3,4}}), "P4: five nodes");
    check(1, ref_tree_diameter(2, {{0,1}}), "P4: two nodes");
    check(0, ref_tree_diameter(1, {}), "P4: single");
    check(2, ref_tree_diameter(5, {{0,1},{0,2},{0,3},{0,4}}), "P4: star");

    // P5: Unique Digits
    check(19, ref_unique_digits(20), "P5: twenty");
    check(90, ref_unique_digits(100), "P5: hundred");
    check(10, ref_unique_digits(10), "P5: ten");
    check(1, ref_unique_digits(1), "P5: one");

    // C1: Merge Stones
    check(20, ref_merge_stones({3,2,4,1}, 2), "C1: k=2");
    check(25, ref_merge_stones({3,5,1,2,6}, 3), "C1: k=3");
    check(-1, ref_merge_stones({3,2,4,1}, 3), "C1: impossible");
    check(0, ref_merge_stones({5}, 2), "C1: single");

    // C2: Wear Hats
    check(2, ref_wear_hats(2, {{1,2},{1,2}}), "C2: two same");
    check(4, ref_wear_hats(2, {{1,2,3},{1,2}}), "C2: two diff");
    check(1, ref_wear_hats(1, {{1}}), "C2: single");
    check(4, ref_wear_hats(3, {{1,2},{2,3},{3,4}}), "C2: three people");

    // C3: Cameras
    check(2, ref_cameras(5, {{0,1},{0,2},{1,3},{1,4}}), "C3: five nodes");
    check(1, ref_cameras(3, {{0,1},{1,2}}), "C3: chain");
    check(1, ref_cameras(1, {}), "C3: single");
    check(1, ref_cameras(2, {{0,1}}), "C3: two nodes");

    // C4: Palindrome Partition
    check(1, ref_palindrome_partition("aab"), "C4: aab");
    check(0, ref_palindrome_partition("a"), "C4: single");
    check(1, ref_palindrome_partition("ab"), "C4: ab");
    check(1, ref_palindrome_partition("aabb"), "C4: aabb");
    check(0, ref_palindrome_partition("aba"), "C4: palindrome");

    cout << endl;
    if (failed_count == 0) {
        printf("All %d ch31 C++ tests passed!\n", passed);
    } else {
        printf("%d passed, %d failed.\n", passed, failed_count);
        return 1;
    }
    return 0;
}
