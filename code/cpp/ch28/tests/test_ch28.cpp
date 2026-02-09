/*
 * Tests for Chapter 28: Topological Sort — Ordering Dependencies
 * Build: g++ -std=c++17 -o /tmp/test_ch28 code/cpp/ch28/tests/test_ch28.cpp && /tmp/test_ch28
 */

#include <algorithm>
#include <cassert>
#include <climits>
#include <functional>
#include <iostream>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions (uniquely named with ref_ prefix)
// =====================================================================

// W1: Topological Sort (Kahn's)
vector<int> ref_topo_sort(int n, vector<vector<int>> edges) {
    vector<vector<int>> adj(n);
    vector<int> inDeg(n, 0);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        inDeg[e[1]]++;
    }
    queue<int> q;
    for (int i = 0; i < n; i++)
        if (inDeg[i] == 0) q.push(i);
    vector<int> result;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        result.push_back(u);
        for (int v : adj[u])
            if (--inDeg[v] == 0) q.push(v);
    }
    return (int)result.size() == n ? result : vector<int>{};
}

// W2: Course Schedule I
bool ref_course_schedule(int numCourses, vector<vector<int>> prereqs) {
    vector<vector<int>> adj(numCourses);
    vector<int> inDeg(numCourses, 0);
    for (auto& p : prereqs) { adj[p[1]].push_back(p[0]); inDeg[p[0]]++; }
    queue<int> q;
    for (int i = 0; i < numCourses; i++)
        if (inDeg[i] == 0) q.push(i);
    int count = 0;
    while (!q.empty()) {
        int u = q.front(); q.pop(); count++;
        for (int v : adj[u]) if (--inDeg[v] == 0) q.push(v);
    }
    return count == numCourses;
}

// W3: Course Schedule II
vector<int> ref_course_schedule_ii(int numCourses, vector<vector<int>> prereqs) {
    vector<vector<int>> adj(numCourses);
    vector<int> inDeg(numCourses, 0);
    for (auto& p : prereqs) { adj[p[1]].push_back(p[0]); inDeg[p[0]]++; }
    queue<int> q;
    for (int i = 0; i < numCourses; i++)
        if (inDeg[i] == 0) q.push(i);
    vector<int> result;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        result.push_back(u);
        for (int v : adj[u]) if (--inDeg[v] == 0) q.push(v);
    }
    return (int)result.size() == numCourses ? result : vector<int>{};
}

// W4: Detect Cycle
bool ref_detect_cycle(int n, vector<vector<int>> edges) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) adj[e[0]].push_back(e[1]);
    vector<int> color(n, 0);
    function<bool(int)> hasCycle = [&](int u) -> bool {
        color[u] = 1;
        for (int v : adj[u]) {
            if (color[v] == 1) return true;
            if (color[v] == 0 && hasCycle(v)) return true;
        }
        color[u] = 2;
        return false;
    };
    for (int i = 0; i < n; i++)
        if (color[i] == 0 && hasCycle(i)) return false;
    return true;
}

// P1: Alien Dictionary
string ref_alien_dict(vector<string> words) {
    unordered_set<char> chars;
    for (auto& w : words) for (char c : w) chars.insert(c);
    unordered_map<char, unordered_set<char>> adj;
    unordered_map<char, int> inDeg;
    for (char c : chars) inDeg[c] = 0;
    for (int i = 0; i < (int)words.size() - 1; i++) {
        if (words[i].size() > words[i+1].size() &&
            words[i].substr(0, words[i+1].size()) == words[i+1]) return "";
        int len = min(words[i].size(), words[i+1].size());
        for (int j = 0; j < len; j++) {
            if (words[i][j] != words[i+1][j]) {
                if (!adj[words[i][j]].count(words[i+1][j])) {
                    adj[words[i][j]].insert(words[i+1][j]);
                    inDeg[words[i+1][j]]++;
                }
                break;
            }
        }
    }
    queue<char> q;
    for (char c : chars) if (inDeg[c] == 0) q.push(c);
    string result;
    while (!q.empty()) {
        char c = q.front(); q.pop(); result += c;
        for (char nxt : adj[c]) if (--inDeg[nxt] == 0) q.push(nxt);
    }
    return result.size() == chars.size() ? result : "";
}

// P2: Parallel Courses
int ref_parallel_courses(int n, vector<vector<int>> relations) {
    vector<vector<int>> adj(n + 1);
    vector<int> inDeg(n + 1, 0);
    for (auto& r : relations) { adj[r[0]].push_back(r[1]); inDeg[r[1]]++; }
    queue<int> q;
    for (int i = 1; i <= n; i++) if (inDeg[i] == 0) q.push(i);
    int sem = 0, cnt = 0;
    while (!q.empty()) {
        sem++; int sz = q.size();
        for (int i = 0; i < sz; i++) {
            int u = q.front(); q.pop(); cnt++;
            for (int v : adj[u]) if (--inDeg[v] == 0) q.push(v);
        }
    }
    return cnt == n ? sem : -1;
}

// P3: Find All Recipes
vector<string> ref_find_recipes(vector<string> recipes, vector<vector<string>> ingredients,
                                vector<string> supplies) {
    unordered_set<string> recipeSet(recipes.begin(), recipes.end());
    unordered_map<string, vector<string>> adj;
    unordered_map<string, int> inDeg;
    for (int i = 0; i < (int)recipes.size(); i++) {
        inDeg[recipes[i]] = 0;
        for (auto& ing : ingredients[i]) {
            adj[ing].push_back(recipes[i]);
            inDeg[recipes[i]]++;
        }
    }
    queue<string> q;
    unordered_set<string> seen(supplies.begin(), supplies.end());
    for (auto& s : supplies) q.push(s);
    vector<string> result;
    while (!q.empty()) {
        string item = q.front(); q.pop();
        if (recipeSet.count(item)) result.push_back(item);
        if (adj.count(item))
            for (auto& nxt : adj[item])
                if (--inDeg[nxt] == 0 && !seen.count(nxt)) { seen.insert(nxt); q.push(nxt); }
    }
    return result;
}

// P4: All Ancestors
vector<vector<int>> ref_all_ancestors(int n, vector<vector<int>> edges) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) adj[e[0]].push_back(e[1]);
    vector<set<int>> ancestors(n);
    for (int u = 0; u < n; u++) {
        stack<int> stk; stk.push(u);
        vector<bool> visited(n, false);
        while (!stk.empty()) {
            int node = stk.top(); stk.pop();
            for (int v : adj[node])
                if (!visited[v]) { visited[v] = true; ancestors[v].insert(u); stk.push(v); }
        }
    }
    vector<vector<int>> result(n);
    for (int i = 0; i < n; i++) result[i] = vector<int>(ancestors[i].begin(), ancestors[i].end());
    return result;
}

// C1: Minimum Height Trees
vector<int> ref_mht(int n, vector<vector<int>> edges) {
    if (n == 1) return {0};
    vector<set<int>> adj(n);
    for (auto& e : edges) { adj[e[0]].insert(e[1]); adj[e[1]].insert(e[0]); }
    queue<int> leaves;
    for (int i = 0; i < n; i++) if ((int)adj[i].size() == 1) leaves.push(i);
    int remaining = n;
    while (remaining > 2) {
        int sz = leaves.size(); remaining -= sz;
        queue<int> newLeaves;
        for (int i = 0; i < sz; i++) {
            int leaf = leaves.front(); leaves.pop();
            for (int nb : adj[leaf]) { adj[nb].erase(leaf); if ((int)adj[nb].size() == 1) newLeaves.push(nb); }
        }
        leaves = newLeaves;
    }
    vector<int> result;
    while (!leaves.empty()) { result.push_back(leaves.front()); leaves.pop(); }
    return result;
}

// C2: Eventual Safe States
vector<int> ref_safe_states(vector<vector<int>> graph) {
    int n = graph.size();
    vector<int> color(n, 0);
    function<bool(int)> isSafe = [&](int u) -> bool {
        if (color[u] == 1) return false;
        if (color[u] == 2) return true;
        color[u] = 1;
        for (int v : graph[u]) if (!isSafe(v)) return false;
        color[u] = 2;
        return true;
    };
    vector<int> result;
    for (int i = 0; i < n; i++) if (isSafe(i)) result.push_back(i);
    return result;
}

// C3: Largest Color Value
int ref_largest_color(string colors, vector<vector<int>> edges) {
    int n = colors.size();
    vector<vector<int>> adj(n);
    vector<int> inDeg(n, 0);
    for (auto& e : edges) { adj[e[0]].push_back(e[1]); inDeg[e[1]]++; }
    vector<vector<int>> dp(n, vector<int>(26, 0));
    queue<int> q;
    for (int i = 0; i < n; i++) if (inDeg[i] == 0) q.push(i);
    int count = 0, result = 0;
    while (!q.empty()) {
        int u = q.front(); q.pop(); count++;
        dp[u][colors[u] - 'a']++;
        for (int c = 0; c < 26; c++) result = max(result, dp[u][c]);
        for (int v : adj[u]) {
            for (int c = 0; c < 26; c++) dp[v][c] = max(dp[v][c], dp[u][c]);
            if (--inDeg[v] == 0) q.push(v);
        }
    }
    return count == n ? result : -1;
}

// =====================================================================
// Helpers
// =====================================================================

bool is_valid_topo(int n, vector<vector<int>>& edges, vector<int>& order) {
    if ((int)order.size() != n) return false;
    unordered_map<int, int> pos;
    for (int i = 0; i < n; i++) pos[order[i]] = i;
    if ((int)pos.size() != n) return false;
    for (auto& e : edges)
        if (pos[e[0]] >= pos[e[1]]) return false;
    return true;
}

bool is_valid_alien(vector<string>& words, string& order) {
    if (order.empty()) return false;
    unordered_map<char, int> pos;
    for (int i = 0; i < (int)order.size(); i++) pos[order[i]] = i;
    for (int i = 0; i < (int)words.size() - 1; i++) {
        bool foundDiff = false;
        int len = min(words[i].size(), words[i+1].size());
        for (int j = 0; j < len; j++) {
            if (words[i][j] != words[i+1][j]) {
                if (pos[words[i][j]] >= pos[words[i+1][j]]) return false;
                foundDiff = true; break;
            }
        }
        if (!foundDiff && words[i].size() > words[i+1].size()) return false;
    }
    return true;
}

// =====================================================================
// Test runner
// =====================================================================

int passed = 0, failed_cnt = 0;

void check(bool condition, const string& msg) {
    if (condition) { passed++; }
    else { failed_cnt++; cout << "FAIL: " << msg << endl; }
}

void check_int(int expected, int actual, const string& msg) {
    if (expected == actual) { passed++; }
    else { failed_cnt++; cout << "FAIL: " << msg << " — expected " << expected << ", got " << actual << endl; }
}

void check_bool(bool expected, bool actual, const string& msg) {
    if (expected == actual) { passed++; }
    else { failed_cnt++; cout << "FAIL: " << msg << " — expected " << expected << ", got " << actual << endl; }
}

void check_vec(vector<int> expected, vector<int> actual, const string& msg) {
    if (expected == actual) { passed++; }
    else {
        failed_cnt++;
        cout << "FAIL: " << msg << " — expected [";
        for (int i = 0; i < (int)expected.size(); i++) cout << (i?",":"") << expected[i];
        cout << "], got [";
        for (int i = 0; i < (int)actual.size(); i++) cout << (i?",":"") << actual[i];
        cout << "]" << endl;
    }
}

int main() {
    cout << "Chapter 28: Topological Sort — Ordering Dependencies" << endl;
    cout << "======================================================" << endl << endl;

    // W1: Topological Sort
    {
        vector<vector<int>> edges = {{5,2},{5,0},{4,0},{4,1},{2,3},{3,1}};
        auto r = ref_topo_sort(6, edges);
        check(is_valid_topo(6, edges, r), "W1: basic");
    }
    {
        vector<vector<int>> edges = {{0,1},{1,2}};
        check_vec({0,1,2}, ref_topo_sort(3, edges), "W1: chain");
    }
    check_vec({0}, ref_topo_sort(1, {}), "W1: single");

    // W2: Course Schedule I
    check_bool(true, ref_course_schedule(2, {{1,0}}), "W2: possible");
    check_bool(false, ref_course_schedule(2, {{1,0},{0,1}}), "W2: cycle");
    check_bool(true, ref_course_schedule(4, {{1,0},{2,1},{3,2}}), "W2: chain");
    check_bool(true, ref_course_schedule(1, {}), "W2: single");

    // W3: Course Schedule II
    {
        vector<vector<int>> prereqs = {{1,0},{2,0},{3,1},{3,2}};
        auto r = ref_course_schedule_ii(4, prereqs);
        // Validate: b must come before a for each [a,b]
        unordered_map<int, int> pos;
        for (int i = 0; i < (int)r.size(); i++) pos[r[i]] = i;
        bool valid = (int)r.size() == 4;
        for (auto& p : prereqs) valid = valid && pos[p[1]] < pos[p[0]];
        check(valid, "W3: basic");
    }
    check_vec({}, ref_course_schedule_ii(2, {{1,0},{0,1}}), "W3: cycle");
    check_vec({0}, ref_course_schedule_ii(1, {}), "W3: single");

    // W4: Detect Cycle
    check_bool(true, ref_detect_cycle(4, {{0,1},{1,2},{2,3}}), "W4: dag");
    check_bool(false, ref_detect_cycle(3, {{0,1},{1,2},{2,0}}), "W4: cycle");
    check_bool(true, ref_detect_cycle(4, {{0,1},{1,2},{3,0}}), "W4: dag branch");
    check_bool(true, ref_detect_cycle(1, {}), "W4: single");

    // P1: Alien Dictionary
    {
        vector<string> w = {"wrt","wrf","er","ett","rftt"};
        string r = ref_alien_dict(w);
        check(is_valid_alien(w, r), "P1: basic");
    }
    {
        vector<string> w = {"z","x"};
        string r = ref_alien_dict(w);
        check(is_valid_alien(w, r), "P1: two");
    }
    check(ref_alien_dict({"z","x","z"}).empty(), "P1: cycle");

    // P2: Parallel Courses
    check_int(2, ref_parallel_courses(3, {{1,3},{2,3}}), "P2: basic");
    check_int(-1, ref_parallel_courses(3, {{1,2},{2,3},{3,1}}), "P2: cycle");
    check_int(3, ref_parallel_courses(4, {{1,2},{1,3},{2,4},{3,4}}), "P2: diamond");

    // P3: Find All Recipes
    {
        auto r = ref_find_recipes({"bread","sandwich"}, {{"yeast","flour"},{"bread","meat"}},
                                  {"yeast","flour","meat"});
        sort(r.begin(), r.end());
        check(r == vector<string>{"bread","sandwich"}, "P3: chain");
    }
    {
        auto r = ref_find_recipes({"bread"}, {{"yeast","flour"}}, {"yeast"});
        check(r.empty(), "P3: missing");
    }

    // P4: All Ancestors
    {
        auto r = ref_all_ancestors(5, {{0,1},{0,2},{0,3},{1,4},{2,4}});
        check_vec({}, r[0], "P4: node 0");
        check_vec({0}, r[1], "P4: node 1");
        check_vec({0}, r[2], "P4: node 2");
        check_vec({0}, r[3], "P4: node 3");
        check_vec({0,1,2}, r[4], "P4: node 4");
    }
    {
        auto r = ref_all_ancestors(3, {{0,1},{1,2}});
        check_vec({}, r[0], "P4: chain 0");
        check_vec({0}, r[1], "P4: chain 1");
        check_vec({0,1}, r[2], "P4: chain 2");
    }

    // C1: Minimum Height Trees
    {
        auto r = ref_mht(4, {{1,0},{1,2},{1,3}});
        sort(r.begin(), r.end());
        check_vec({1}, r, "C1: star");
    }
    {
        auto r = ref_mht(6, {{3,0},{3,1},{3,2},{3,4},{5,4}});
        sort(r.begin(), r.end());
        check_vec({3,4}, r, "C1: path");
    }
    check_vec({0}, ref_mht(1, {}), "C1: single");
    {
        auto r = ref_mht(2, {{0,1}});
        sort(r.begin(), r.end());
        check_vec({0,1}, r, "C1: pair");
    }

    // C2: Eventual Safe States
    check_vec({2,4,5,6}, ref_safe_states({{1,2},{2,3},{5},{0},{5},{},{}}), "C2: basic");
    check_vec({4}, ref_safe_states({{1,2,3,4},{1,2},{3,4},{0,4},{}}), "C2: cycle heavy");

    // C3: Largest Color Value
    check_int(3, ref_largest_color("abaca", {{0,1},{0,2},{2,3},{3,4}}), "C3: basic");
    check_int(-1, ref_largest_color("a", {{0,0}}), "C3: self loop");
    check_int(1, ref_largest_color("a", {}), "C3: single");

    cout << endl;
    if (failed_cnt == 0) {
        printf("All %d ch28 C++ tests passed!\n", passed);
    } else {
        printf("%d passed, %d failed.\n", passed, failed_cnt);
        return 1;
    }
    return 0;
}
