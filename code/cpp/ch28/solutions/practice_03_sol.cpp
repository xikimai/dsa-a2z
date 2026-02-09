/*
 * Solution for Practice 3: Find All Recipes
 * Chapter 28: Topological Sort — Ordering Dependencies
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

vector<string> solve(vector<string>& recipes, vector<vector<string>>& ingredients,
                     vector<string>& supplies) {
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
        if (adj.count(item)) {
            for (auto& nxt : adj[item]) {
                inDeg[nxt]--;
                if (inDeg[nxt] == 0 && !seen.count(nxt)) {
                    seen.insert(nxt);
                    q.push(nxt);
                }
            }
        }
    }
    return result;
}

int main() { return 0; }
