/*
 * Tests for Chapter 19: Graphs I — Exploring Networks
 * Build: g++ -std=c++17 -o /tmp/test_ch19 code/cpp/ch19/tests/test_ch19.cpp && /tmp/test_ch19
 */

#include <algorithm>
#include <cassert>
#include <iostream>
#include <queue>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions (uniquely named with ref_ prefix)
// =====================================================================

// --- W1: Build Adjacency List ---
vector<vector<int>> ref_build_adj_list(int n, vector<vector<int>> edges) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }
    for (auto& nbrs : adj) sort(nbrs.begin(), nbrs.end());
    return adj;
}

// --- W2: BFS Traversal ---
vector<int> ref_bfs_traversal(int n, vector<vector<int>> edges, int source) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }
    vector<bool> visited(n, false);
    visited[source] = true;
    queue<int> q;
    q.push(source);
    vector<int> order;
    while (!q.empty()) {
        int node = q.front(); q.pop();
        order.push_back(node);
        vector<int> nbrs = adj[node];
        sort(nbrs.begin(), nbrs.end());
        for (int nb : nbrs) {
            if (!visited[nb]) { visited[nb] = true; q.push(nb); }
        }
    }
    return order;
}

// --- W3: DFS Traversal ---
void ref_dfs_helper(vector<vector<int>>& adj, int node, vector<bool>& visited, vector<int>& order) {
    visited[node] = true;
    order.push_back(node);
    vector<int> nbrs = adj[node];
    sort(nbrs.begin(), nbrs.end());
    for (int nb : nbrs) {
        if (!visited[nb]) ref_dfs_helper(adj, nb, visited, order);
    }
}

vector<int> ref_dfs_traversal(int n, vector<vector<int>> edges, int source) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }
    vector<bool> visited(n, false);
    vector<int> order;
    ref_dfs_helper(adj, source, visited, order);
    return order;
}

// --- W4: Count Components ---
int ref_count_components(int n, vector<vector<int>> edges) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }
    vector<bool> visited(n, false);
    int count = 0;
    for (int v = 0; v < n; v++) {
        if (!visited[v]) {
            queue<int> q;
            q.push(v);
            visited[v] = true;
            while (!q.empty()) {
                int node = q.front(); q.pop();
                for (int nb : adj[node]) {
                    if (!visited[nb]) { visited[nb] = true; q.push(nb); }
                }
            }
            count++;
        }
    }
    return count;
}

// --- W5: Is Path Exists ---
bool ref_is_path_exists(int n, vector<vector<int>> edges, int source, int dest) {
    if (source == dest) return true;
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }
    vector<bool> visited(n, false);
    visited[source] = true;
    queue<int> q;
    q.push(source);
    while (!q.empty()) {
        int node = q.front(); q.pop();
        for (int nb : adj[node]) {
            if (nb == dest) return true;
            if (!visited[nb]) { visited[nb] = true; q.push(nb); }
        }
    }
    return false;
}

// --- P1: Shortest Path ---
vector<int> ref_shortest_path(int n, vector<vector<int>> edges, int source) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }
    vector<int> dist(n, -1);
    dist[source] = 0;
    queue<int> q;
    q.push(source);
    while (!q.empty()) {
        int node = q.front(); q.pop();
        for (int nb : adj[node]) {
            if (dist[nb] == -1) { dist[nb] = dist[node] + 1; q.push(nb); }
        }
    }
    return dist;
}

// --- P2: Detect Cycle ---
bool ref_dfs_cycle(vector<vector<int>>& adj, int node, int parent, vector<bool>& visited) {
    visited[node] = true;
    for (int nb : adj[node]) {
        if (!visited[nb]) {
            if (ref_dfs_cycle(adj, nb, node, visited)) return true;
        } else if (nb != parent) return true;
    }
    return false;
}

bool ref_detect_cycle(int n, vector<vector<int>> edges) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }
    vector<bool> visited(n, false);
    for (int v = 0; v < n; v++) {
        if (!visited[v] && ref_dfs_cycle(adj, v, -1, visited)) return true;
    }
    return false;
}

// --- P3: Bipartite Check ---
bool ref_bipartite(int n, vector<vector<int>> edges) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }
    vector<int> color(n, -1);
    for (int start = 0; start < n; start++) {
        if (color[start] != -1) continue;
        color[start] = 0;
        queue<int> q;
        q.push(start);
        while (!q.empty()) {
            int node = q.front(); q.pop();
            for (int nb : adj[node]) {
                if (color[nb] == -1) { color[nb] = 1 - color[node]; q.push(nb); }
                else if (color[nb] == color[node]) return false;
            }
        }
    }
    return true;
}

// --- P4: Clone Graph ---
vector<vector<int>> ref_clone_graph(vector<vector<int>> adj) {
    vector<vector<int>> clone;
    for (auto& nbrs : adj) clone.push_back(vector<int>(nbrs.begin(), nbrs.end()));
    return clone;
}

// --- P5: All Paths ---
void ref_all_paths_dfs(vector<vector<int>>& adj, int node, int target,
                        vector<int>& path, vector<vector<int>>& result) {
    if (node == target) { result.push_back(path); return; }
    vector<int> nbrs = adj[node];
    sort(nbrs.begin(), nbrs.end());
    for (int nb : nbrs) {
        path.push_back(nb);
        ref_all_paths_dfs(adj, nb, target, path, result);
        path.pop_back();
    }
}

vector<vector<int>> ref_all_paths(int n, vector<vector<int>> edges) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) adj[e[0]].push_back(e[1]);
    vector<vector<int>> result;
    vector<int> path = {0};
    ref_all_paths_dfs(adj, 0, n - 1, path, result);
    sort(result.begin(), result.end());
    return result;
}

// --- C1: Number of Provinces ---
int ref_num_provinces(vector<vector<int>> isConnected) {
    int n = isConnected.size();
    vector<bool> visited(n, false);
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            queue<int> q;
            q.push(i);
            visited[i] = true;
            while (!q.empty()) {
                int city = q.front(); q.pop();
                for (int j = 0; j < n; j++) {
                    if (isConnected[city][j] == 1 && !visited[j]) {
                        visited[j] = true;
                        q.push(j);
                    }
                }
            }
            count++;
        }
    }
    return count;
}

// --- C2: Course Schedule ---
bool ref_has_cycle(vector<vector<int>>& adj, int node, vector<int>& state) {
    state[node] = 1;
    for (int nb : adj[node]) {
        if (state[nb] == 1) return true;
        if (state[nb] == 0 && ref_has_cycle(adj, nb, state)) return true;
    }
    state[node] = 2;
    return false;
}

bool ref_course_schedule(int numCourses, vector<vector<int>> prerequisites) {
    vector<vector<int>> adj(numCourses);
    for (auto& p : prerequisites) adj[p[1]].push_back(p[0]);
    vector<int> state(numCourses, 0);
    for (int c = 0; c < numCourses; c++) {
        if (state[c] == 0 && ref_has_cycle(adj, c, state)) return false;
    }
    return true;
}

// --- C3: Word Ladder ---
int ref_word_ladder(string beginWord, string endWord, vector<string> wordList) {
    unordered_set<string> wordSet(wordList.begin(), wordList.end());
    if (!wordSet.count(endWord)) return 0;
    queue<pair<string, int>> q;
    q.push({beginWord, 1});
    unordered_set<string> visited;
    visited.insert(beginWord);
    while (!q.empty()) {
        auto [word, length] = q.front(); q.pop();
        if (word == endWord) return length;
        for (int i = 0; i < (int)word.size(); i++) {
            char original = word[i];
            for (char c = 'a'; c <= 'z'; c++) {
                if (c == original) continue;
                word[i] = c;
                if (wordSet.count(word) && !visited.count(word)) {
                    visited.insert(word);
                    q.push({word, length + 1});
                }
            }
            word[i] = original;
        }
    }
    return 0;
}

// =====================================================================
// Test runner
// =====================================================================

int passed = 0, failed = 0;

void check(bool condition, const string& msg) {
    if (condition) { passed++; }
    else { failed++; cout << "FAIL: " << msg << endl; }
}

int main() {
    cout << "Chapter 19: Graphs I — Exploring Networks" << endl;
    cout << "==========================================" << endl << endl;

    // W1
    check(ref_build_adj_list(4, {{0,1},{0,2},{1,3}})[0] == vector<int>({1,2}), "W1: node 0");
    check(ref_build_adj_list(4, {{0,1},{0,2},{1,3}})[2] == vector<int>({0}), "W1: node 2");
    check(ref_build_adj_list(3, {})[0] == vector<int>({}), "W1: no edges");
    check(ref_build_adj_list(1, {})[0] == vector<int>({}), "W1: single node");

    // W2
    check(ref_bfs_traversal(5, {{0,1},{0,2},{1,3},{2,3},{3,4}}, 0) == vector<int>({0,1,2,3,4}), "W2: basic");
    check(ref_bfs_traversal(3, {{0,1},{1,2}}, 2) == vector<int>({2,1,0}), "W2: from end");
    check(ref_bfs_traversal(1, {}, 0) == vector<int>({0}), "W2: single");
    check(ref_bfs_traversal(4, {{0,1},{2,3}}, 0) == vector<int>({0,1}), "W2: disconnected");

    // W3
    check(ref_dfs_traversal(5, {{0,1},{0,2},{1,3},{2,3},{3,4}}, 0) == vector<int>({0,1,3,2,4}), "W3: basic");
    check(ref_dfs_traversal(3, {{0,1},{1,2}}, 0) == vector<int>({0,1,2}), "W3: linear");
    check(ref_dfs_traversal(1, {}, 0) == vector<int>({0}), "W3: single");
    check(ref_dfs_traversal(4, {{0,1},{1,2},{2,3}}, 1) == vector<int>({1,0,2,3}), "W3: from middle");

    // W4
    check(ref_count_components(5, {{0,1},{1,2},{3,4}}) == 2, "W4: two");
    check(ref_count_components(4, {}) == 4, "W4: no edges");
    check(ref_count_components(3, {{0,1},{1,2},{0,2}}) == 1, "W4: full");
    check(ref_count_components(1, {}) == 1, "W4: single");
    check(ref_count_components(7, {{0,1},{0,2},{3,4},{3,5}}) == 3, "W4: three");

    // W5
    check(ref_is_path_exists(5, {{0,1},{1,2},{3,4}}, 0, 2) == true, "W5: exists");
    check(ref_is_path_exists(5, {{0,1},{1,2},{3,4}}, 0, 4) == false, "W5: no path");
    check(ref_is_path_exists(3, {}, 0, 0) == true, "W5: same");
    check(ref_is_path_exists(3, {{0,1},{1,2}}, 0, 1) == true, "W5: direct");
    check(ref_is_path_exists(3, {{0,1}}, 0, 2) == false, "W5: isolated");

    // P1
    check(ref_shortest_path(5, {{0,1},{0,2},{1,3},{2,3},{3,4}}, 0) == vector<int>({0,1,1,2,3}), "P1: basic");
    check(ref_shortest_path(4, {{0,1},{2,3}}, 0) == vector<int>({0,1,-1,-1}), "P1: disconnected");
    check(ref_shortest_path(1, {}, 0) == vector<int>({0}), "P1: single");
    check(ref_shortest_path(4, {{0,1},{1,2},{2,3}}, 0) == vector<int>({0,1,2,3}), "P1: linear");
    check(ref_shortest_path(5, {{0,1},{1,2},{2,3},{3,4}}, 2) == vector<int>({2,1,0,1,2}), "P1: middle");

    // P2
    check(ref_detect_cycle(4, {{0,1},{1,2},{2,3}}) == false, "P2: no cycle");
    check(ref_detect_cycle(4, {{0,1},{1,2},{2,3},{3,0}}) == true, "P2: has cycle");
    check(ref_detect_cycle(3, {{0,1},{1,2},{0,2}}) == true, "P2: triangle");
    check(ref_detect_cycle(3, {}) == false, "P2: no edges");
    check(ref_detect_cycle(5, {{0,1},{2,3},{3,4},{4,2}}) == true, "P2: disc w/ cycle");
    check(ref_detect_cycle(5, {{0,1},{2,3}}) == false, "P2: disc no cycle");

    // P3
    check(ref_bipartite(4, {{0,1},{1,2},{2,3},{3,0}}) == true, "P3: even cycle");
    check(ref_bipartite(3, {{0,1},{1,2},{0,2}}) == false, "P3: triangle");
    check(ref_bipartite(3, {}) == true, "P3: no edges");
    check(ref_bipartite(2, {{0,1}}) == true, "P3: single edge");
    check(ref_bipartite(5, {{0,1},{2,3}}) == true, "P3: disc bipartite");
    check(ref_bipartite(5, {{0,1},{1,2},{2,3},{3,4},{4,0}}) == false, "P3: 5-cycle");

    // P4
    vector<vector<int>> adj4 = {{1,2},{0,3},{0,3},{1,2}};
    auto clone4 = ref_clone_graph(adj4);
    check(clone4 == adj4, "P4: content match");
    check(ref_clone_graph({}).empty(), "P4: empty");
    check(ref_clone_graph({{}}) == vector<vector<int>>({{}}), "P4: single node");

    // P5
    check(ref_all_paths(4, {{0,1},{0,2},{1,3},{2,3}}) ==
        vector<vector<int>>({{0,1,3},{0,2,3}}), "P5: basic");
    check(ref_all_paths(4, {{0,1},{0,2},{1,2},{1,3},{2,3}}) ==
        vector<vector<int>>({{0,1,2,3},{0,1,3},{0,2,3}}), "P5: multiple");
    check(ref_all_paths(2, {{0,1}}) == vector<vector<int>>({{0,1}}), "P5: direct");
    check(ref_all_paths(3, {{0,1}}).empty(), "P5: no path");

    // C1
    check(ref_num_provinces({{1,1,0},{1,1,0},{0,0,1}}) == 2, "C1: two");
    check(ref_num_provinces({{1,0,0},{0,1,0},{0,0,1}}) == 3, "C1: three");
    check(ref_num_provinces({{1,1,1},{1,1,1},{1,1,1}}) == 1, "C1: one");
    check(ref_num_provinces({{1}}) == 1, "C1: single");

    // C2
    check(ref_course_schedule(2, {{1,0}}) == true, "C2: no cycle");
    check(ref_course_schedule(2, {{1,0},{0,1}}) == false, "C2: cycle");
    check(ref_course_schedule(4, {{1,0},{2,1},{3,2}}) == true, "C2: chain");
    check(ref_course_schedule(3, {}) == true, "C2: no prereqs");
    check(ref_course_schedule(4, {{1,0},{2,1},{0,2}}) == false, "C2: complex");
    check(ref_course_schedule(4, {{1,0},{3,2}}) == true, "C2: disconnected");

    // C3
    check(ref_word_ladder("hit", "cog", {"hot","dot","dog","lot","log","cog"}) == 5, "C3: basic");
    check(ref_word_ladder("hit", "cog", {"hot","dot","dog","lot","log"}) == 0, "C3: no path");
    check(ref_word_ladder("hot", "dot", {"dot"}) == 2, "C3: direct");
    check(ref_word_ladder("a", "c", {"a","b","c"}) == 2, "C3: single letter");
    check(ref_word_ladder("abc", "xyz", {"abd","acd"}) == 0, "C3: end not in list");

    cout << endl;
    if (failed == 0) {
        cout << "All " << passed << " tests passed!" << endl;
    } else {
        cout << passed << " passed, " << failed << " failed." << endl;
        return 1;
    }
    return 0;
}
