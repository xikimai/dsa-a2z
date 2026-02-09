/*
 * Solution for Challenge 2: Find Eventual Safe States
 * Chapter 28: Topological Sort — Ordering Dependencies
 */
#include <algorithm>
#include <climits>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> solve(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> color(n, 0); // 0=white, 1=gray, 2=black

    function<bool(int)> isSafe = [&](int u) -> bool {
        if (color[u] == 1) return false;
        if (color[u] == 2) return true;
        color[u] = 1;
        for (int v : graph[u])
            if (!isSafe(v)) return false;
        color[u] = 2;
        return true;
    };

    vector<int> result;
    for (int i = 0; i < n; i++)
        if (isSafe(i)) result.push_back(i);
    return result;
}

int main() { return 0; }
