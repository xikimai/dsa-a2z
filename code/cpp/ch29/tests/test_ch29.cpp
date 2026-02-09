/*
 * Tests for Chapter 29: Union-Find & Minimum Spanning Trees
 * Build: g++ -std=c++17 -o /tmp/test_ch29 code/cpp/ch29/tests/test_ch29.cpp && /tmp/test_ch29
 */

#include <algorithm>
#include <cassert>
#include <climits>
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

// W1: Connected Components
int ref_connected_components(int n, vector<vector<int>> edges) {
    vector<int> parent(n), rnk(n, 0);
    iota(parent.begin(), parent.end(), 0);
    function<int(int)> find = [&](int x) -> int {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };
    int comp = n;
    for (auto& e : edges) {
        int rx = find(e[0]), ry = find(e[1]);
        if (rx != ry) {
            if (rnk[rx] < rnk[ry]) parent[rx] = ry;
            else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
            else { parent[ry] = rx; rnk[rx]++; }
            comp--;
        }
    }
    return comp;
}

// W2: Redundant Connection (1-indexed)
vector<int> ref_redundant_connection(vector<vector<int>> edges) {
    int n = edges.size();
    vector<int> parent(n + 1), rnk(n + 1, 0);
    iota(parent.begin(), parent.end(), 0);
    function<int(int)> find = [&](int x) -> int {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };
    for (auto& e : edges) {
        int rx = find(e[0]), ry = find(e[1]);
        if (rx == ry) return e;
        if (rnk[rx] < rnk[ry]) parent[rx] = ry;
        else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
        else { parent[ry] = rx; rnk[rx]++; }
    }
    return {};
}

// W3: Kruskal's MST
int ref_kruskal(int n, vector<vector<int>> edges) {
    if (n <= 1) return 0;
    vector<int> parent(n), rnk(n, 0);
    iota(parent.begin(), parent.end(), 0);
    function<int(int)> find = [&](int x) -> int {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };
    sort(edges.begin(), edges.end(), [](auto& a, auto& b) { return a[2] < b[2]; });
    int total = 0;
    for (auto& e : edges) {
        int rx = find(e[0]), ry = find(e[1]);
        if (rx != ry) {
            if (rnk[rx] < rnk[ry]) parent[rx] = ry;
            else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
            else { parent[ry] = rx; rnk[rx]++; }
            total += e[2];
        }
    }
    return total;
}

// W4: Prim's MST
int ref_prim(int n, vector<vector<int>> edges) {
    if (n <= 1) return 0;
    vector<vector<pair<int,int>>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back({e[2], e[1]});
        adj[e[1]].push_back({e[2], e[0]});
    }
    vector<bool> vis(n, false);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0, 0});
    int total = 0, count = 0;
    while (!pq.empty() && count < n) {
        auto [w, u] = pq.top(); pq.pop();
        if (vis[u]) continue;
        vis[u] = true;
        total += w;
        count++;
        for (auto [nw, nv] : adj[u])
            if (!vis[nv]) pq.push({nw, nv});
    }
    return total;
}

// P1: Number of Provinces
int ref_provinces(vector<vector<int>> isConnected) {
    int n = isConnected.size();
    vector<int> parent(n), rnk(n, 0);
    iota(parent.begin(), parent.end(), 0);
    function<int(int)> find = [&](int x) -> int {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };
    int comp = n;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (isConnected[i][j] == 1) {
                int rx = find(i), ry = find(j);
                if (rx != ry) {
                    if (rnk[rx] < rnk[ry]) parent[rx] = ry;
                    else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
                    else { parent[ry] = rx; rnk[rx]++; }
                    comp--;
                }
            }
    return comp;
}

// P3: Most Stones Removed
int ref_stones(vector<vector<int>> stones) {
    if (stones.empty()) return 0;
    unordered_map<int, int> parent, rnk;
    function<int(int)> find = [&](int x) -> int {
        if (parent.find(x) == parent.end()) { parent[x] = x; rnk[x] = 0; }
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };
    auto unite = [&](int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return;
        if (rnk[rx] < rnk[ry]) parent[rx] = ry;
        else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
        else { parent[ry] = rx; rnk[rx]++; }
    };
    for (auto& s : stones) unite(s[0], s[1] + 10001);
    unordered_set<int> comps;
    for (auto& s : stones) comps.insert(find(s[0]));
    return (int)stones.size() - (int)comps.size();
}

// P4: Min Cost Connect Points
int ref_min_cost_points(vector<vector<int>> points) {
    int n = points.size();
    if (n <= 1) return 0;
    vector<int> parent(n), rnk(n, 0);
    iota(parent.begin(), parent.end(), 0);
    function<int(int)> find = [&](int x) -> int {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };
    vector<tuple<int,int,int>> edges;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            edges.push_back({abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]), i, j});
    sort(edges.begin(), edges.end());
    int total = 0;
    for (auto [w, u, v] : edges) {
        int rx = find(u), ry = find(v);
        if (rx != ry) {
            if (rnk[rx] < rnk[ry]) parent[rx] = ry;
            else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
            else { parent[ry] = rx; rnk[rx]++; }
            total += w;
        }
    }
    return total;
}

// P5: Satisfiability of Equality Equations
bool ref_equations(vector<string> equations) {
    vector<int> parent(26), rnk(26, 0);
    iota(parent.begin(), parent.end(), 0);
    function<int(int)> find = [&](int x) -> int {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };
    auto unite = [&](int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return;
        if (rnk[rx] < rnk[ry]) parent[rx] = ry;
        else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
        else { parent[ry] = rx; rnk[rx]++; }
    };
    for (auto& eq : equations)
        if (eq[1] == '=') unite(eq[0]-'a', eq[3]-'a');
    for (auto& eq : equations)
        if (eq[1] == '!')
            if (find(eq[0]-'a') == find(eq[3]-'a')) return false;
    return true;
}

// C1: Make Network Connected
int ref_make_connected(int n, vector<vector<int>> connections) {
    if ((int)connections.size() < n - 1) return -1;
    vector<int> parent(n), rnk(n, 0);
    iota(parent.begin(), parent.end(), 0);
    function<int(int)> find = [&](int x) -> int {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };
    int comp = n;
    for (auto& c : connections) {
        int rx = find(c[0]), ry = find(c[1]);
        if (rx != ry) {
            if (rnk[rx] < rnk[ry]) parent[rx] = ry;
            else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
            else { parent[ry] = rx; rnk[rx]++; }
            comp--;
        }
    }
    return comp - 1;
}

// C2: Making a Large Island
int ref_large_island(vector<vector<int>> grid) {
    int n = grid.size();
    vector<int> parent(n*n), rnk(n*n, 0), sz(n*n, 1);
    for (int i = 0; i < n*n; i++) parent[i] = i;
    function<int(int)> find = [&](int x) -> int {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };
    auto unite = [&](int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return;
        if (rnk[rx] < rnk[ry]) { parent[rx] = ry; sz[ry] += sz[rx]; }
        else if (rnk[rx] > rnk[ry]) { parent[ry] = rx; sz[rx] += sz[ry]; }
        else { parent[ry] = rx; sz[rx] += sz[ry]; rnk[rx]++; }
    };
    int dirs2[][2] = {{0,1},{1,0}};
    for (int r = 0; r < n; r++)
        for (int c = 0; c < n; c++)
            if (grid[r][c] == 1)
                for (auto& d : dirs2) {
                    int nr = r+d[0], nc = c+d[1];
                    if (nr < n && nc < n && grid[nr][nc] == 1)
                        unite(r*n+c, nr*n+nc);
                }
    int best = 0;
    for (int r = 0; r < n; r++)
        for (int c = 0; c < n; c++)
            if (grid[r][c] == 1) best = max(best, sz[find(r*n+c)]);
    int dirs4[][2] = {{-1,0},{1,0},{0,-1},{0,1}};
    for (int r = 0; r < n; r++)
        for (int c = 0; c < n; c++)
            if (grid[r][c] == 0) {
                set<int> seen;
                int total = 1;
                for (auto& d : dirs4) {
                    int nr = r+d[0], nc = c+d[1];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                        int root = find(nr*n+nc);
                        if (seen.insert(root).second) total += sz[root];
                    }
                }
                best = max(best, total);
            }
    return best;
}

// C3: Number of Islands II
vector<int> ref_islands_ii(int m, int n, vector<vector<int>> positions) {
    vector<int> parent(m*n, -1), rnk(m*n, 0);
    function<int(int)> find = [&](int x) -> int {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };
    int count = 0;
    vector<int> result;
    int dirs[][2] = {{-1,0},{1,0},{0,-1},{0,1}};
    for (auto& pos : positions) {
        int r = pos[0], c = pos[1], idx = r*n+c;
        if (parent[idx] != -1) { result.push_back(count); continue; }
        parent[idx] = idx;
        count++;
        for (auto& d : dirs) {
            int nr = r+d[0], nc = c+d[1], nidx = nr*n+nc;
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && parent[nidx] != -1) {
                int rx = find(idx), ry = find(nidx);
                if (rx != ry) {
                    if (rnk[rx] < rnk[ry]) parent[rx] = ry;
                    else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
                    else { parent[ry] = rx; rnk[rx]++; }
                    count--;
                }
            }
        }
        result.push_back(count);
    }
    return result;
}

// C4: Smallest String With Swaps
string ref_smallest_string_swaps(string s, vector<vector<int>> pairs) {
    int n = s.size();
    vector<int> parent(n), rnk(n, 0);
    iota(parent.begin(), parent.end(), 0);
    function<int(int)> find = [&](int x) -> int {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };
    auto unite = [&](int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return;
        if (rnk[rx] < rnk[ry]) parent[rx] = ry;
        else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
        else { parent[ry] = rx; rnk[rx]++; }
    };
    for (auto& p : pairs) unite(p[0], p[1]);
    map<int, vector<int>> groups;
    for (int i = 0; i < n; i++) groups[find(i)].push_back(i);
    string result = s;
    for (auto& [root, indices] : groups) {
        string chars;
        for (int i : indices) chars += s[i];
        sort(chars.begin(), chars.end());
        sort(indices.begin(), indices.end());
        for (int k = 0; k < (int)indices.size(); k++)
            result[indices[k]] = chars[k];
    }
    return result;
}

// =====================================================================
// Test runner
// =====================================================================

int passed = 0, failed_count = 0;

void check(int expected, int actual, const string& msg) {
    if (expected == actual) { passed++; }
    else { failed_count++; cout << "FAIL: " << msg << " — expected " << expected << ", got " << actual << endl; }
}

void check_bool(bool expected, bool actual, const string& msg) {
    if (expected == actual) { passed++; }
    else { failed_count++; cout << "FAIL: " << msg << " — expected " << expected << ", got " << actual << endl; }
}

void check_vec(vector<int> expected, vector<int> actual, const string& msg) {
    if (expected == actual) { passed++; }
    else {
        failed_count++;
        cout << "FAIL: " << msg << " — expected [";
        for (int i = 0; i < (int)expected.size(); i++) cout << (i?",":"") << expected[i];
        cout << "], got [";
        for (int i = 0; i < (int)actual.size(); i++) cout << (i?",":"") << actual[i];
        cout << "]" << endl;
    }
}

void check_str(const string& expected, const string& actual, const string& msg) {
    if (expected == actual) { passed++; }
    else { failed_count++; cout << "FAIL: " << msg << " — expected '" << expected << "', got '" << actual << "'" << endl; }
}

int main() {
    cout << "Chapter 29: Union-Find & Minimum Spanning Trees" << endl;
    cout << "================================================================" << endl << endl;

    // W1: Connected Components
    check(2, ref_connected_components(5, {{0,1},{1,2},{3,4}}), "W1: two components");
    check(5, ref_connected_components(5, {}), "W1: all isolated");
    check(1, ref_connected_components(4, {{0,1},{1,2},{2,3}}), "W1: single chain");
    check(1, ref_connected_components(3, {{0,1},{0,2},{1,2}}), "W1: with cycle");

    // W2: Redundant Connection
    check_vec({2,3}, ref_redundant_connection({{1,2},{1,3},{2,3}}), "W2: triangle");
    check_vec({1,4}, ref_redundant_connection({{1,2},{2,3},{3,4},{1,4},{1,5}}), "W2: longer");

    // W3: Kruskal's MST
    check(19, ref_kruskal(4, {{0,1,10},{0,2,6},{0,3,5},{1,3,15},{2,3,4}}), "W3: basic");
    check(3, ref_kruskal(3, {{0,1,1},{1,2,2},{0,2,3}}), "W3: triangle");
    check(0, ref_kruskal(1, {}), "W3: single node");

    // W4: Prim's MST
    check(19, ref_prim(4, {{0,1,10},{0,2,6},{0,3,5},{1,3,15},{2,3,4}}), "W4: basic");
    check(3, ref_prim(3, {{0,1,1},{1,2,2},{0,2,3}}), "W4: triangle");
    check(0, ref_prim(1, {}), "W4: single node");

    // P1: Provinces
    check(2, ref_provinces({{1,1,0},{1,1,0},{0,0,1}}), "P1: two provinces");
    check(3, ref_provinces({{1,0,0},{0,1,0},{0,0,1}}), "P1: all isolated");
    check(1, ref_provinces({{1,1,1},{1,1,1},{1,1,1}}), "P1: all connected");

    // P3: Most Stones Removed
    check(5, ref_stones({{0,0},{0,1},{1,0},{1,2},{2,1},{2,2}}), "P3: grid");
    check(3, ref_stones({{0,0},{0,2},{1,1},{2,0},{2,2}}), "P3: diagonal");
    check(0, ref_stones({{0,0}}), "P3: single");

    // P4: Min Cost Connect Points
    check(20, ref_min_cost_points({{0,0},{2,2},{3,10},{5,2},{7,0}}), "P4: basic");
    check(18, ref_min_cost_points({{3,12},{-2,5},{-4,1}}), "P4: three points");
    check(0, ref_min_cost_points({{0,0}}), "P4: single");

    // P5: Equations
    check_bool(false, ref_equations({"a==b","b!=a"}), "P5: contradiction");
    check_bool(true, ref_equations({"b==a","a==b"}), "P5: consistent");
    check_bool(true, ref_equations({"a==b","b==c","a==c"}), "P5: transitive");
    check_bool(false, ref_equations({"a==b","b!=c","c==a"}), "P5: transitive contradiction");

    // C1: Make Connected
    check(1, ref_make_connected(4, {{0,1},{0,2},{1,2}}), "C1: one spare");
    check(2, ref_make_connected(6, {{0,1},{0,2},{0,3},{1,2},{1,3}}), "C1: two spare");
    check(-1, ref_make_connected(4, {{0,1},{0,2}}), "C1: impossible");

    // C2: Large Island
    check(3, ref_large_island({{1,0},{0,1}}), "C2: diagonal");
    check(4, ref_large_island({{1,1},{1,0}}), "C2: one zero");
    check(4, ref_large_island({{1,1},{1,1}}), "C2: all ones");

    // C3: Islands II
    check_vec({1,1,2,3}, ref_islands_ii(3, 3, {{0,0},{0,1},{1,2},{2,1}}), "C3: basic");
    check_vec({1}, ref_islands_ii(1, 1, {{0,0}}), "C3: single");

    // C4: Smallest String Swaps
    check_str("bacd", ref_smallest_string_swaps("dcab", {{0,3},{1,2}}), "C4: two groups");
    check_str("abcd", ref_smallest_string_swaps("dcab", {{0,3},{1,2},{0,2}}), "C4: all connected");
    check_str("abc", ref_smallest_string_swaps("cba", {{0,1},{1,2}}), "C4: chain");

    cout << endl;
    if (failed_count == 0) {
        printf("All %d ch29 C++ tests passed!\n", passed);
    } else {
        printf("%d passed, %d failed.\n", passed, failed_count);
        return 1;
    }
    return 0;
}
