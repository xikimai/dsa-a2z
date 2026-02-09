/*
 * Tests for Chapter 27: Shortest Paths — Finding the Best Route
 * Build: g++ -std=c++17 -o /tmp/test_ch27 code/cpp/ch27/tests/test_ch27.cpp && /tmp/test_ch27
 */

#include <algorithm>
#include <cassert>
#include <climits>
#include <deque>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

static int passed = 0, failed = 0;

void check(bool cond, const string& msg) {
    if (cond) { passed++; }
    else { failed++; cout << "FAIL: " << msg << "\n"; }
}

// =====================================================================
// Reference solutions (uniquely named with ref_ prefix)
// =====================================================================

// W1: Dijkstra SSSP
vector<int> ref_dijkstra(int n, vector<vector<int>> edges, int src) {
    const int INF = 1e9;
    vector<vector<pair<int,int>>> adj(n);
    for (auto& e : edges) adj[e[0]].push_back({e[1], e[2]});
    vector<int> dist(n, INF);
    dist[src] = 0;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0, src});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto [v, w] : adj[u])
            if (dist[u] + w < dist[v]) { dist[v] = dist[u] + w; pq.push({dist[v], v}); }
    }
    return dist;
}

// W2: Network Delay
int ref_network_delay(vector<vector<int>> times, int n, int k) {
    const int INF = 1e9;
    vector<vector<pair<int,int>>> adj(n + 1);
    for (auto& t : times) adj[t[0]].push_back({t[1], t[2]});
    vector<int> dist(n + 1, INF);
    dist[k] = 0;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0, k});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto [v, w] : adj[u])
            if (dist[u] + w < dist[v]) { dist[v] = dist[u] + w; pq.push({dist[v], v}); }
    }
    int ans = *max_element(dist.begin() + 1, dist.end());
    return ans >= INF ? -1 : ans;
}

// W3: Bellman-Ford
vector<int> ref_bellman_ford(int n, vector<vector<int>> edges, int src) {
    const int INF = 1e9;
    vector<int> dist(n, INF);
    dist[src] = 0;
    for (int i = 0; i < n - 1; i++)
        for (auto& e : edges)
            if (dist[e[0]] != INF && dist[e[0]] + e[2] < dist[e[1]])
                dist[e[1]] = dist[e[0]] + e[2];
    return dist;
}

// W4: Binary Matrix BFS
int ref_binary_matrix(vector<vector<int>> grid) {
    int n = grid.size();
    if (grid[0][0] == 1 || grid[n-1][n-1] == 1) return -1;
    if (n == 1) return 1;
    int dirs[][2] = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
    deque<tuple<int,int,int>> q;
    q.push_back({0, 0, 1});
    grid[0][0] = 1;
    while (!q.empty()) {
        auto [r, c, len] = q.front(); q.pop_front();
        for (auto& d : dirs) {
            int nr = r+d[0], nc = c+d[1];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                if (nr == n-1 && nc == n-1) return len + 1;
                grid[nr][nc] = 1;
                q.push_back({nr, nc, len + 1});
            }
        }
    }
    return -1;
}

// P1: Cheapest Flights
int ref_cheapest_flights(int n, vector<vector<int>> flights, int src, int dst, int k) {
    const int INF = 1e9;
    vector<int> dist(n, INF);
    dist[src] = 0;
    for (int i = 0; i <= k; i++) {
        vector<int> prev = dist;
        for (auto& f : flights)
            if (prev[f[0]] != INF && prev[f[0]] + f[2] < dist[f[1]])
                dist[f[1]] = prev[f[0]] + f[2];
    }
    return dist[dst] >= INF ? -1 : dist[dst];
}

// P2: Min Effort
int ref_min_effort(vector<vector<int>> heights) {
    int m = heights.size(), n = heights[0].size();
    const int INF = 1e9;
    vector<vector<int>> dist(m, vector<int>(n, INF));
    dist[0][0] = 0;
    priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, greater<>> pq;
    pq.push({0, 0, 0});
    int dirs[][2] = {{0,1},{0,-1},{1,0},{-1,0}};
    while (!pq.empty()) {
        auto [e, r, c] = pq.top(); pq.pop();
        if (e > dist[r][c]) continue;
        if (r == m-1 && c == n-1) return e;
        for (auto& d : dirs) {
            int nr = r+d[0], nc = c+d[1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                int ne = max(e, abs(heights[r][c] - heights[nr][nc]));
                if (ne < dist[nr][nc]) { dist[nr][nc] = ne; pq.push({ne, nr, nc}); }
            }
        }
    }
    return dist[m-1][n-1];
}

// P3: City Threshold (Floyd-Warshall)
int ref_city_threshold(int n, vector<vector<int>> edges, int threshold) {
    const int INF = 1e9;
    vector<vector<int>> dist(n, vector<int>(n, INF));
    for (int i = 0; i < n; i++) dist[i][i] = 0;
    for (auto& e : edges) {
        dist[e[0]][e[1]] = min(dist[e[0]][e[1]], e[2]);
        dist[e[1]][e[0]] = min(dist[e[1]][e[0]], e[2]);
    }
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
    int bestCity = -1, bestCount = n + 1;
    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = 0; j < n; j++) if (j != i && dist[i][j] <= threshold) count++;
        if (count <= bestCount) { bestCount = count; bestCity = i; }
    }
    return bestCity;
}

// P4: Count Paths
int ref_count_paths(int n, vector<vector<int>> roads) {
    const long long MOD = 1e9 + 7, INF = 1e18;
    vector<vector<pair<int,long long>>> adj(n);
    for (auto& r : roads) { adj[r[0]].push_back({r[1],r[2]}); adj[r[1]].push_back({r[0],r[2]}); }
    vector<long long> dist(n, INF), ways(n, 0);
    dist[0] = 0; ways[0] = 1;
    priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<>> pq;
    pq.push({0, 0});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto [v, w] : adj[u]) {
            long long nd = dist[u] + w;
            if (nd < dist[v]) { dist[v] = nd; ways[v] = ways[u]; pq.push({nd, v}); }
            else if (nd == dist[v]) ways[v] = (ways[v] + ways[u]) % MOD;
        }
    }
    return (int)(ways[n-1] % MOD);
}

// P5: Swim Rising
int ref_swim_rising(vector<vector<int>> grid) {
    int n = grid.size();
    const int INF = 1e9;
    vector<vector<int>> dist(n, vector<int>(n, INF));
    dist[0][0] = grid[0][0];
    priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, greater<>> pq;
    pq.push({grid[0][0], 0, 0});
    int dirs[][2] = {{0,1},{0,-1},{1,0},{-1,0}};
    while (!pq.empty()) {
        auto [d, r, c] = pq.top(); pq.pop();
        if (d > dist[r][c]) continue;
        if (r == n-1 && c == n-1) return d;
        for (auto& dir : dirs) {
            int nr = r+dir[0], nc = c+dir[1];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                int nd = max(d, grid[nr][nc]);
                if (nd < dist[nr][nc]) { dist[nr][nc] = nd; pq.push({nd, nr, nc}); }
            }
        }
    }
    return dist[n-1][n-1];
}

// C1: Obstacle Removal (0-1 BFS)
int ref_obstacle_removal(vector<vector<int>> grid) {
    int m = grid.size(), n = grid[0].size();
    const int INF = 1e9;
    vector<vector<int>> dist(m, vector<int>(n, INF));
    dist[0][0] = 0;
    deque<pair<int,int>> dq;
    dq.push_front({0, 0});
    int dirs[][2] = {{0,1},{0,-1},{1,0},{-1,0}};
    while (!dq.empty()) {
        auto [r, c] = dq.front(); dq.pop_front();
        for (auto& d : dirs) {
            int nr = r+d[0], nc = c+d[1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                int cost = grid[nr][nc];
                if (dist[r][c] + cost < dist[nr][nc]) {
                    dist[nr][nc] = dist[r][c] + cost;
                    if (cost == 0) dq.push_front({nr, nc}); else dq.push_back({nr, nc});
                }
            }
        }
    }
    return dist[m-1][n-1];
}

// C2: Alternating Colors
vector<int> ref_alternating(int n, vector<vector<int>> red, vector<vector<int>> blue) {
    const int INF = 1e9;
    vector<vector<vector<int>>> adj(n, vector<vector<int>>(2));
    for (auto& e : red) adj[e[0]][0].push_back(e[1]);
    for (auto& e : blue) adj[e[0]][1].push_back(e[1]);
    vector<vector<int>> dist(n, vector<int>(2, INF));
    dist[0][0] = 0; dist[0][1] = 0;
    deque<pair<int,int>> q;
    q.push_back({0, 0}); q.push_back({0, 1});
    while (!q.empty()) {
        auto [u, color] = q.front(); q.pop_front();
        int nc = 1 - color;
        for (int v : adj[u][nc])
            if (dist[u][color] + 1 < dist[v][nc]) { dist[v][nc] = dist[u][color] + 1; q.push_back({v, nc}); }
    }
    vector<int> res(n);
    for (int i = 0; i < n; i++) { int b = min(dist[i][0], dist[i][1]); res[i] = b >= INF ? -1 : b; }
    return res;
}

// C3: Valid Path (0-1 BFS)
int ref_valid_path(vector<vector<int>> grid) {
    int m = grid.size(), n = grid[0].size();
    int arrowDir[][2] = {{0,0},{0,1},{0,-1},{1,0},{-1,0}};
    int dirs[][2] = {{0,1},{0,-1},{1,0},{-1,0}};
    const int INF = 1e9;
    vector<vector<int>> dist(m, vector<int>(n, INF));
    dist[0][0] = 0;
    deque<pair<int,int>> dq;
    dq.push_front({0, 0});
    while (!dq.empty()) {
        auto [r, c] = dq.front(); dq.pop_front();
        int arrow = grid[r][c];
        int adr = arrowDir[arrow][0], adc = arrowDir[arrow][1];
        for (auto& d : dirs) {
            int nr = r+d[0], nc = c+d[1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                int cost = (d[0] == adr && d[1] == adc) ? 0 : 1;
                if (dist[r][c] + cost < dist[nr][nc]) {
                    dist[nr][nc] = dist[r][c] + cost;
                    if (cost == 0) dq.push_front({nr, nc}); else dq.push_back({nr, nc});
                }
            }
        }
    }
    return dist[m-1][n-1];
}

// C4: Max Min Path
int ref_max_min_path(vector<vector<int>> grid) {
    int m = grid.size(), n = grid[0].size();
    vector<vector<int>> dist(m, vector<int>(n, -1));
    dist[0][0] = grid[0][0];
    priority_queue<tuple<int,int,int>> pq;
    pq.push({grid[0][0], 0, 0});
    int dirs[][2] = {{0,1},{0,-1},{1,0},{-1,0}};
    while (!pq.empty()) {
        auto [d, r, c] = pq.top(); pq.pop();
        if (d < dist[r][c]) continue;
        if (r == m-1 && c == n-1) return d;
        for (auto& dir : dirs) {
            int nr = r+dir[0], nc = c+dir[1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                int nv = min(d, grid[nr][nc]);
                if (nv > dist[nr][nc]) { dist[nr][nc] = nv; pq.push({nv, nr, nc}); }
            }
        }
    }
    return dist[m-1][n-1];
}

// =====================================================================
// Test functions
// =====================================================================

void testW1() {
    check(ref_dijkstra(5, {{0,1,4},{0,2,1},{2,1,2},{1,3,5},{2,3,8},{3,4,1}}, 0)
        == vector<int>({0,3,1,8,9}), "W1: basic");
    check(ref_dijkstra(3, {{0,1,1},{1,2,2}}, 0) == vector<int>({0,1,3}), "W1: linear");
    check(ref_dijkstra(1, {}, 0) == vector<int>({0}), "W1: single");
}

void testW2() {
    check(ref_network_delay({{2,1,1},{2,3,1},{3,4,1}}, 4, 2) == 2, "W2: basic");
    check(ref_network_delay({{1,2,1}}, 2, 2) == -1, "W2: unreachable");
    check(ref_network_delay({{1,2,1}}, 2, 1) == 1, "W2: single edge");
}

void testW3() {
    check(ref_bellman_ford(5, {{0,1,-1},{0,2,4},{1,2,3},{1,3,2},{1,4,2},{3,2,5},{3,1,1},{4,3,-3}}, 0)
        == vector<int>({0,-1,2,-2,1}), "W3: negative");
    check(ref_bellman_ford(3, {{0,1,4},{0,2,1},{2,1,2}}, 0) == vector<int>({0,3,1}), "W3: positive");
}

void testW4() {
    check(ref_binary_matrix({{0,1},{1,0}}) == 2, "W4: 2x2");
    check(ref_binary_matrix({{0,0,0},{1,1,0},{1,1,0}}) == 4, "W4: 3x3");
    check(ref_binary_matrix({{1,0,0},{0,0,0},{0,0,0}}) == -1, "W4: blocked");
    check(ref_binary_matrix({{0}}) == 1, "W4: single");
}

void testP1() {
    check(ref_cheapest_flights(4, {{0,1,100},{1,2,100},{2,0,100},{1,3,600},{2,3,200}}, 0, 3, 1) == 700, "P1: basic");
    check(ref_cheapest_flights(3, {{0,1,100},{1,2,100},{0,2,500}}, 0, 2, 1) == 200, "P1: via stop");
    check(ref_cheapest_flights(3, {{0,1,100},{1,2,100},{0,2,500}}, 0, 2, 0) == 500, "P1: no stops");
}

void testP2() {
    check(ref_min_effort({{1,2,2},{3,8,2},{5,3,5}}) == 2, "P2: basic");
    check(ref_min_effort({{1,2,3},{3,8,4},{5,3,5}}) == 1, "P2: small diff");
    check(ref_min_effort({{1,2,1,1,1},{1,2,1,2,1},{1,2,1,2,1},{1,2,1,2,1},{1,1,1,2,1}}) == 0, "P2: zero");
}

void testP3() {
    check(ref_city_threshold(4, {{0,1,3},{1,2,1},{1,3,4},{2,3,1}}, 4) == 3, "P3: basic");
    check(ref_city_threshold(5, {{0,1,2},{0,4,8},{1,2,3},{1,4,2},{2,3,1},{3,4,1}}, 2) == 0, "P3: larger");
}

void testP4() {
    check(ref_count_paths(7, {{0,6,7},{0,1,2},{1,2,3},{1,3,3},{6,3,3},{3,5,1},{6,5,1},{2,5,1},{0,4,5},{4,6,2}}) == 4, "P4: basic");
    check(ref_count_paths(2, {{1,0,10}}) == 1, "P4: two nodes");
}

void testP5() {
    check(ref_swim_rising({{0,2},{1,3}}) == 3, "P5: 2x2");
    check(ref_swim_rising({{0,1,2,3,4},{24,23,22,21,5},{12,13,14,15,16},{11,17,18,19,20},{10,9,8,7,6}}) == 16, "P5: 5x5");
}

void testC1() {
    check(ref_obstacle_removal({{0,1,1},{1,1,0},{1,1,0}}) == 2, "C1: basic");
    check(ref_obstacle_removal({{0,1,0,0,0},{0,1,0,1,0},{0,0,0,1,0}}) == 0, "C1: clear");
}

void testC2() {
    check(ref_alternating(3, {{0,1},{1,2}}, {}) == vector<int>({0,1,-1}), "C2: red only");
    check(ref_alternating(3, {{0,1}}, {{2,1}}) == vector<int>({0,1,-1}), "C2: mixed");
    check(ref_alternating(3, {{0,1},{0,2}}, {{1,0}}) == vector<int>({0,1,1}), "C2: both");
}

void testC3() {
    check(ref_valid_path({{1,1,2},{1,1,2},{1,1,1}}) == 2, "C3: needs changes");
    check(ref_valid_path({{1,1,3},{3,2,2},{1,1,4}}) == 0, "C3: free");
    check(ref_valid_path({{2,2,2},{2,2,2}}) == 3, "C3: all left");
}

void testC4() {
    check(ref_max_min_path({{5,4,5},{1,2,6},{7,4,6}}) == 4, "C4: basic");
    check(ref_max_min_path({{2,2,1,2,2,2},{1,2,2,2,1,2}}) == 2, "C4: narrow");
    check(ref_max_min_path({{3,4,6,3,4},{0,2,1,1,7},{8,8,3,2,7},{3,2,4,9,8},{4,1,2,0,0},{4,6,5,4,3}}) == 3, "C4: larger");
}

int main() {
    cout << "Chapter 27: Shortest Paths — Finding the Best Route\n";
    cout << "====================================================\n\n";

    testW1(); testW2(); testW3(); testW4();
    testP1(); testP2(); testP3(); testP4(); testP5();
    testC1(); testC2(); testC3(); testC4();

    cout << "\n";
    if (failed == 0)
        cout << "All " << passed << " tests passed!\n";
    else {
        cout << passed << " passed, " << failed << " failed.\n";
        return 1;
    }
    return 0;
}
