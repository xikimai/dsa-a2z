/*
 * Tests for Chapter 33: Advanced Trees & Graph Algorithms
 * Build: g++ -std=c++17 -o /tmp/test_ch33 code/cpp/ch33/tests/test_ch33.cpp && /tmp/test_ch33
 */

#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
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

// W1: LCA with Binary Lifting
vector<int> ref_lca_binary_lifting(int n, vector<vector<int>> edges, vector<vector<int>> queries) {
    if (n == 1) return vector<int>(queries.size(), 0);
    vector<vector<int>> adj(n);
    for (auto& e : edges) { adj[e[0]].push_back(e[1]); adj[e[1]].push_back(e[0]); }

    int LOG = max(1, (int)ceil(log2(n)) + 1);
    vector<vector<int>> up(n, vector<int>(LOG, -1));
    vector<int> depth(n, 0);

    vector<bool> visited(n, false);
    queue<int> q;
    q.push(0); visited[0] = true;
    while (!q.empty()) {
        int node = q.front(); q.pop();
        for (int nb : adj[node]) {
            if (!visited[nb]) {
                visited[nb] = true;
                depth[nb] = depth[node] + 1;
                up[nb][0] = node;
                q.push(nb);
            }
        }
    }
    for (int k = 1; k < LOG; k++)
        for (int v = 0; v < n; v++)
            if (up[v][k-1] != -1) up[v][k] = up[up[v][k-1]][k-1];

    auto lca = [&](int u, int v) -> int {
        if (depth[u] < depth[v]) swap(u, v);
        int diff = depth[u] - depth[v];
        for (int k = 0; k < LOG; k++)
            if ((diff >> k) & 1) u = up[u][k];
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; k--)
            if (up[u][k] != up[v][k]) { u = up[u][k]; v = up[v][k]; }
        return up[u][0];
    };

    vector<int> result;
    for (auto& qr : queries) result.push_back(lca(qr[0], qr[1]));
    return result;
}

// W2: Euler Tour
vector<int> ref_euler_tour(int n, vector<vector<int>> edges) {
    if (n == 1) return {0};
    vector<vector<int>> adj(n);
    for (auto& e : edges) { adj[e[0]].push_back(e[1]); adj[e[1]].push_back(e[0]); }
    for (auto& a : adj) sort(a.begin(), a.end());

    vector<int> order;
    vector<bool> visited(n, false);
    // Iterative DFS
    vector<int> stk = {0};
    visited[0] = true;
    while (!stk.empty()) {
        int node = stk.back(); stk.pop_back();
        order.push_back(node);
        for (int i = (int)adj[node].size() - 1; i >= 0; i--) {
            int nb = adj[node][i];
            if (!visited[nb]) { visited[nb] = true; stk.push_back(nb); }
        }
    }
    return order;
}

// W3: Bridges
vector<vector<int>> ref_bridges(int n, vector<vector<int>> edges) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) { adj[e[0]].push_back(e[1]); adj[e[1]].push_back(e[0]); }

    vector<int> disc(n, -1), low(n, 0);
    vector<vector<int>> bridges;
    int timer = 0;

    function<void(int,int)> dfs = [&](int u, int parent) {
        disc[u] = low[u] = timer++;
        for (int v : adj[u]) {
            if (disc[v] == -1) {
                dfs(v, u);
                low[u] = min(low[u], low[v]);
                if (low[v] > disc[u])
                    bridges.push_back({min(u,v), max(u,v)});
            } else if (v != parent) {
                low[u] = min(low[u], disc[v]);
            }
        }
    };
    for (int i = 0; i < n; i++)
        if (disc[i] == -1) dfs(i, -1);
    sort(bridges.begin(), bridges.end());
    return bridges;
}

// P1: Articulation Points
vector<int> ref_articulation_points(int n, vector<vector<int>> edges) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) { adj[e[0]].push_back(e[1]); adj[e[1]].push_back(e[0]); }

    vector<int> disc(n, -1), low(n, 0);
    set<int> ap;
    int timer = 0;

    function<void(int,int)> dfs = [&](int u, int parent) {
        disc[u] = low[u] = timer++;
        int children = 0;
        for (int v : adj[u]) {
            if (disc[v] == -1) {
                children++;
                dfs(v, u);
                low[u] = min(low[u], low[v]);
                if (parent == -1 && children > 1) ap.insert(u);
                if (parent != -1 && low[v] >= disc[u]) ap.insert(u);
            } else if (v != parent) {
                low[u] = min(low[u], disc[v]);
            }
        }
    };
    for (int i = 0; i < n; i++)
        if (disc[i] == -1) dfs(i, -1);
    return vector<int>(ap.begin(), ap.end());
}

// P2: SCC Count (Kosaraju's)
int ref_scc_count(int n, vector<vector<int>> edges) {
    vector<vector<int>> adj(n), radj(n);
    for (auto& e : edges) { adj[e[0]].push_back(e[1]); radj[e[1]].push_back(e[0]); }

    vector<bool> visited(n, false);
    vector<int> order;
    function<void(int)> dfs1 = [&](int u) {
        visited[u] = true;
        for (int v : adj[u]) if (!visited[v]) dfs1(v);
        order.push_back(u);
    };
    for (int i = 0; i < n; i++) if (!visited[i]) dfs1(i);

    vector<int> comp(n, -1);
    int count = 0;
    function<void(int,int)> dfs2 = [&](int u, int label) {
        comp[u] = label;
        for (int v : radj[u]) if (comp[v] == -1) dfs2(v, label);
    };
    for (int i = n - 1; i >= 0; i--)
        if (comp[order[i]] == -1) dfs2(order[i], count++);
    return count;
}

// P3: Subtree Sum
vector<int> ref_subtree_sum(int n, vector<int> values, vector<vector<int>> edges, vector<int> queries) {
    if (n == 1) return vector<int>(queries.size(), values[0]);
    vector<vector<int>> adj(n);
    for (auto& e : edges) { adj[e[0]].push_back(e[1]); adj[e[1]].push_back(e[0]); }

    vector<int> tin(n), tout(n), order;
    int timer = 0;
    function<void(int,int)> dfs = [&](int node, int parent) {
        tin[node] = timer;
        order.push_back(node);
        timer++;
        for (int nb : adj[node])
            if (nb != parent) dfs(nb, node);
        tout[node] = timer - 1;
    };
    dfs(0, -1);

    vector<long long> prefix(n + 1, 0);
    for (int i = 0; i < n; i++)
        prefix[i + 1] = prefix[i] + values[order[i]];

    vector<int> result;
    for (int q : queries)
        result.push_back((int)(prefix[tout[q] + 1] - prefix[tin[q]]));
    return result;
}

// P4: LCA Values
vector<int> ref_lca_values(int n, vector<int> values, vector<vector<int>> edges, vector<vector<int>> queries) {
    if (n == 1) return vector<int>(queries.size(), values[0]);
    vector<vector<int>> adj(n);
    for (auto& e : edges) { adj[e[0]].push_back(e[1]); adj[e[1]].push_back(e[0]); }

    int LOG = max(1, (int)ceil(log2(n)) + 1);
    vector<vector<int>> up(n, vector<int>(LOG, -1));
    vector<int> depth(n, 0);

    vector<bool> visited(n, false);
    queue<int> q;
    q.push(0); visited[0] = true;
    while (!q.empty()) {
        int node = q.front(); q.pop();
        for (int nb : adj[node]) {
            if (!visited[nb]) {
                visited[nb] = true;
                depth[nb] = depth[node] + 1;
                up[nb][0] = node;
                q.push(nb);
            }
        }
    }
    for (int k = 1; k < LOG; k++)
        for (int v = 0; v < n; v++)
            if (up[v][k-1] != -1) up[v][k] = up[up[v][k-1]][k-1];

    auto lca = [&](int u, int v) -> int {
        if (depth[u] < depth[v]) swap(u, v);
        int diff = depth[u] - depth[v];
        for (int k = 0; k < LOG; k++)
            if ((diff >> k) & 1) u = up[u][k];
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; k--)
            if (up[u][k] != up[v][k]) { u = up[u][k]; v = up[v][k]; }
        return up[u][0];
    };

    vector<int> result;
    for (auto& qr : queries) result.push_back(values[lca(qr[0], qr[1])]);
    return result;
}

// P5: Count SCCs of Size > 1
int ref_scc_size_gt1(int n, vector<vector<int>> edges) {
    vector<vector<int>> adj(n), radj(n);
    for (auto& e : edges) { adj[e[0]].push_back(e[1]); radj[e[1]].push_back(e[0]); }

    vector<bool> visited(n, false);
    vector<int> order;
    function<void(int)> dfs1 = [&](int u) {
        visited[u] = true;
        for (int v : adj[u]) if (!visited[v]) dfs1(v);
        order.push_back(u);
    };
    for (int i = 0; i < n; i++) if (!visited[i]) dfs1(i);

    vector<int> comp(n, -1);
    int count = 0;
    function<void(int,int)> dfs2 = [&](int u, int label) {
        comp[u] = label;
        for (int v : radj[u]) if (comp[v] == -1) dfs2(v, label);
    };
    for (int i = n - 1; i >= 0; i--)
        if (comp[order[i]] == -1) dfs2(order[i], count++);

    vector<int> sizes(count, 0);
    for (int c : comp) sizes[c]++;
    int result = 0;
    for (int s : sizes) if (s > 1) result++;
    return result;
}

// C1: Critical Connections
vector<vector<int>> ref_critical_connections(int n, vector<vector<int>> connections) {
    return ref_bridges(n, connections);
}

// C2: Reorder Routes
int ref_reorder_routes(int n, vector<vector<int>> connections) {
    vector<vector<pair<int,int>>> adj(n);
    for (auto& c : connections) {
        adj[c[0]].push_back({c[1], 1});
        adj[c[1]].push_back({c[0], 0});
    }
    vector<bool> visited(n, false);
    visited[0] = true;
    queue<int> q;
    q.push(0);
    int count = 0;
    while (!q.empty()) {
        int node = q.front(); q.pop();
        for (auto [nb, cost] : adj[node]) {
            if (!visited[nb]) {
                visited[nb] = true;
                count += cost;
                q.push(nb);
            }
        }
    }
    return count;
}

// C3: Tree Distance
vector<int> ref_tree_distance(int n, vector<vector<int>> edges, vector<vector<int>> queries) {
    if (n == 1) return vector<int>(queries.size(), 0);
    vector<vector<pair<int,int>>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back({e[1], e[2]});
        adj[e[1]].push_back({e[0], e[2]});
    }

    int LOG = max(1, (int)ceil(log2(n)) + 1);
    vector<vector<int>> up(n, vector<int>(LOG, -1));
    vector<int> depth(n, 0);
    vector<long long> dist(n, 0);

    vector<bool> visited(n, false);
    queue<int> q;
    q.push(0); visited[0] = true;
    while (!q.empty()) {
        int node = q.front(); q.pop();
        for (auto [nb, w] : adj[node]) {
            if (!visited[nb]) {
                visited[nb] = true;
                depth[nb] = depth[node] + 1;
                dist[nb] = dist[node] + w;
                up[nb][0] = node;
                q.push(nb);
            }
        }
    }
    for (int k = 1; k < LOG; k++)
        for (int v = 0; v < n; v++)
            if (up[v][k-1] != -1) up[v][k] = up[up[v][k-1]][k-1];

    auto lca = [&](int u, int v) -> int {
        if (depth[u] < depth[v]) swap(u, v);
        int diff = depth[u] - depth[v];
        for (int k = 0; k < LOG; k++)
            if ((diff >> k) & 1) u = up[u][k];
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; k--)
            if (up[u][k] != up[v][k]) { u = up[u][k]; v = up[v][k]; }
        return up[u][0];
    };

    vector<int> result;
    for (auto& qr : queries) {
        int l = lca(qr[0], qr[1]);
        result.push_back((int)(dist[qr[0]] + dist[qr[1]] - 2 * dist[l]));
    }
    return result;
}

// C4: SCC Condensation
int ref_scc_condensation(int n, vector<vector<int>> edges) {
    vector<vector<int>> adj(n), radj(n);
    for (auto& e : edges) { adj[e[0]].push_back(e[1]); radj[e[1]].push_back(e[0]); }

    vector<bool> visited(n, false);
    vector<int> order;
    function<void(int)> dfs1 = [&](int u) {
        visited[u] = true;
        for (int v : adj[u]) if (!visited[v]) dfs1(v);
        order.push_back(u);
    };
    for (int i = 0; i < n; i++) if (!visited[i]) dfs1(i);

    vector<int> comp(n, -1);
    int count = 0;
    function<void(int,int)> dfs2 = [&](int u, int label) {
        comp[u] = label;
        for (int v : radj[u]) if (comp[v] == -1) dfs2(v, label);
    };
    for (int i = n - 1; i >= 0; i--)
        if (comp[order[i]] == -1) dfs2(order[i], count++);

    set<pair<int,int>> dagEdges;
    for (auto& e : edges)
        if (comp[e[0]] != comp[e[1]])
            dagEdges.insert({comp[e[0]], comp[e[1]]});
    return (int)dagEdges.size();
}

// =====================================================================
// Test runner
// =====================================================================

int passed_count = 0, failed_count = 0;

void check(int expected, int actual, const string& msg) {
    if (expected == actual) { passed_count++; }
    else { failed_count++; cout << "FAIL: " << msg << " — expected " << expected << ", got " << actual << endl; }
}

void check_vec(vector<int> expected, vector<int> actual, const string& msg) {
    if (expected == actual) { passed_count++; }
    else {
        failed_count++;
        cout << "FAIL: " << msg << " — expected [";
        for (int i = 0; i < (int)expected.size(); i++) cout << (i?",":"") << expected[i];
        cout << "], got [";
        for (int i = 0; i < (int)actual.size(); i++) cout << (i?",":"") << actual[i];
        cout << "]" << endl;
    }
}

void check_vec2d(vector<vector<int>> expected, vector<vector<int>> actual, const string& msg) {
    if (expected == actual) { passed_count++; }
    else {
        failed_count++;
        cout << "FAIL: " << msg << " — sizes " << expected.size() << " vs " << actual.size() << endl;
    }
}

int main() {
    cout << "Chapter 33: Advanced Trees & Graph Algorithms" << endl;
    cout << "================================================================" << endl << endl;

    // W1: LCA Binary Lifting
    check_vec({1,0,2}, ref_lca_binary_lifting(7, {{0,1},{0,2},{1,3},{1,4},{2,5},{2,6}}, {{3,4},{3,6},{5,6}}), "W1: basic");
    check_vec({1,0}, ref_lca_binary_lifting(3, {{0,1},{1,2}}, {{1,2},{0,2}}), "W1: chain");
    check_vec({1}, ref_lca_binary_lifting(3, {{0,1},{0,2}}, {{1,1}}), "W1: same node");
    check_vec({0}, ref_lca_binary_lifting(3, {{0,1},{0,2}}, {{1,2}}), "W1: root query");

    // W2: Euler Tour
    check_vec({0,1,3,4,2}, ref_euler_tour(5, {{0,1},{0,2},{1,3},{1,4}}), "W2: basic");
    check_vec({0,1,2}, ref_euler_tour(3, {{0,1},{0,2}}), "W2: small");
    check_vec({0}, ref_euler_tour(1, {}), "W2: single");
    check_vec({0,1,2,3}, ref_euler_tour(4, {{0,1},{1,2},{2,3}}), "W2: chain");

    // W3: Bridges
    check_vec2d({{1,3},{3,4}}, ref_bridges(5, {{0,1},{1,2},{2,0},{1,3},{3,4}}), "W3: basic");
    check_vec2d({}, ref_bridges(4, {{0,1},{1,2},{2,3},{3,0}}), "W3: cycle");
    check_vec2d({{0,1}}, ref_bridges(2, {{0,1}}), "W3: single edge");
    check_vec2d({{0,1},{1,2},{2,3}}, ref_bridges(4, {{0,1},{1,2},{2,3}}), "W3: all bridges");

    // P1: Articulation Points
    check_vec({1,3}, ref_articulation_points(5, {{0,1},{1,2},{2,0},{1,3},{3,4}}), "P1: basic");
    check_vec({}, ref_articulation_points(4, {{0,1},{1,2},{2,3},{3,0}}), "P1: cycle");
    check_vec({0}, ref_articulation_points(5, {{0,1},{0,2},{0,3},{0,4}}), "P1: star");
    check_vec({1,2}, ref_articulation_points(4, {{0,1},{1,2},{2,3}}), "P1: chain");

    // P2: SCC Count
    check(3, ref_scc_count(5, {{0,1},{1,2},{2,0},{1,3},{3,4}}), "P2: basic");
    check(1, ref_scc_count(4, {{0,1},{1,2},{2,3},{3,0}}), "P2: single scc");
    check(3, ref_scc_count(3, {{0,1},{1,2}}), "P2: all separate");
    check(2, ref_scc_count(4, {{0,1},{1,0},{2,3},{3,2}}), "P2: two sccs");

    // P3: Subtree Sum
    check_vec({15,11,3}, ref_subtree_sum(5, {1,2,3,4,5}, {{0,1},{0,2},{1,3},{1,4}}, {0,1,2}), "P3: basic");
    check_vec({60,20}, ref_subtree_sum(3, {10,20,30}, {{0,1},{0,2}}, {0,1}), "P3: small");
    check_vec({42}, ref_subtree_sum(1, {42}, {}, {0}), "P3: single");
    check_vec({10,15}, ref_subtree_sum(3, {5,10,15}, {{0,1},{0,2}}, {1,2}), "P3: leaf");

    // P4: LCA Values
    check_vec({20,10}, ref_lca_values(5, {10,20,30,40,50}, {{0,1},{0,2},{1,3},{1,4}}, {{3,4},{3,2}}), "P4: basic");
    check_vec({5}, ref_lca_values(3, {5,10,15}, {{0,1},{0,2}}, {{1,2}}), "P4: small");
    check_vec({10}, ref_lca_values(3, {5,10,15}, {{0,1},{0,2}}, {{1,1}}), "P4: same node");
    check_vec({100}, ref_lca_values(4, {100,200,300,400}, {{0,1},{0,2},{2,3}}, {{1,3}}), "P4: root lca");

    // P5: SCC Size > 1
    check(2, ref_scc_size_gt1(7, {{0,1},{1,2},{2,0},{3,4},{4,5},{5,3},{6,0}}), "P5: two large");
    check(0, ref_scc_size_gt1(4, {{0,1},{1,2},{2,3}}), "P5: none");
    check(1, ref_scc_size_gt1(3, {{0,1},{1,0},{2,0}}), "P5: one large");
    check(1, ref_scc_size_gt1(4, {{0,1},{1,2},{2,3},{3,0}}), "P5: single big");

    // C1: Critical Connections
    check_vec2d({{1,3}}, ref_critical_connections(4, {{0,1},{1,2},{2,0},{1,3}}), "C1: basic");
    check_vec2d({{2,4}}, ref_critical_connections(5, {{0,1},{1,2},{2,3},{3,0},{2,4}}), "C1: one bridge");
    check_vec2d({}, ref_critical_connections(3, {{0,1},{1,2},{2,0}}), "C1: no bridges");
    check_vec2d({{0,1},{1,2}}, ref_critical_connections(3, {{0,1},{1,2}}), "C1: all bridges");

    // C2: Reorder Routes
    check(3, ref_reorder_routes(6, {{0,1},{1,3},{2,3},{4,0},{4,5}}), "C2: basic");
    check(0, ref_reorder_routes(3, {{1,0},{2,0}}), "C2: all toward");
    check(2, ref_reorder_routes(3, {{0,1},{0,2}}), "C2: all away");
    check(3, ref_reorder_routes(4, {{0,1},{1,2},{2,3}}), "C2: chain");

    // C3: Tree Distance
    check_vec({5,9}, ref_tree_distance(5, {{0,1,2},{0,2,3},{1,3,4},{1,4,1}}, {{3,4},{3,2}}), "C3: basic");
    check_vec({15}, ref_tree_distance(3, {{0,1,5},{0,2,10}}, {{1,2}}), "C3: simple");
    check_vec({0}, ref_tree_distance(3, {{0,1,5},{0,2,10}}, {{1,1}}), "C3: same node");
    check_vec({7}, ref_tree_distance(2, {{0,1,7}}, {{0,1}}), "C3: root query");

    // C4: SCC Condensation
    check(1, ref_scc_condensation(6, {{0,1},{1,2},{2,0},{3,4},{4,5},{5,3},{2,3}}), "C4: two sccs one edge");
    check(1, ref_scc_condensation(4, {{0,1},{1,0},{2,3},{3,2},{1,2}}), "C4: two sccs connected");
    check(2, ref_scc_condensation(3, {{0,1},{1,2}}), "C4: all separate");
    check(0, ref_scc_condensation(3, {{0,1},{1,2},{2,0}}), "C4: single scc");

    cout << endl;
    if (failed_count == 0) {
        printf("All %d ch33 C++ tests passed!\n", passed_count);
    } else {
        printf("%d passed, %d failed.\n", passed_count, failed_count);
        return 1;
    }
    return 0;
}
